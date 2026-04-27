from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

from ..docenv import DocEnv
from ..types import PageRecord
from ..utils import first_non_empty_line, tokenize

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "we",
    "with",
}


def _pick_primary_page(env: DocEnv) -> PageRecord:
    pages = list(env.document.pages)
    if not pages:
        raise ValueError("document has no pages")
    pages.sort(
        key=lambda page: (len(page.words), len(page.text.strip()), len(page.tables)),
        reverse=True,
    )
    return pages[0]


def _nonempty_row_count(rows: Sequence[Sequence[Any]]) -> int:
    return sum(1 for row in rows if any(str(cell).strip() for cell in row))


def _is_numeric_cell(value: Any) -> bool:
    text = str(value).strip()
    if not text:
        return False
    normalized = text.replace(",", "").replace("%", "")
    try:
        float(normalized)
    except ValueError:
        return False
    return True


def _text_cell_count(rows: Sequence[Sequence[Any]]) -> int:
    count = 0
    for row in rows:
        for cell in row:
            text = str(cell).strip()
            if text and not _is_numeric_cell(text):
                count += 1
    return count


def _pick_table_page(env: DocEnv) -> Optional[PageRecord]:
    pages = [page for page in env.document.pages if page.tables]
    if not pages:
        return None
    pages.sort(key=lambda page: len(page.tables), reverse=True)
    return pages[0]


def _pick_best_table(env: DocEnv) -> Optional[Dict[str, Any]]:
    best: Optional[Dict[str, Any]] = None
    for page in env.document.pages:
        for table in page.tables:
            result = env.parse_table(page.page_number, table.bbox)
            rows = result.get("result", {}).get("rows", [])
            nonempty_rows = _nonempty_row_count(rows)
            text_cells = _text_cell_count(rows)
            if result.get("status") != "success" or nonempty_rows < 2 or text_cells < 2:
                continue
            populated_cells = sum(
                1
                for row in rows
                for cell in row
                if str(cell).strip()
            )
            candidate = {
                "page": page,
                "bbox": list(table.bbox),
                "rows": rows,
                "result": result,
                "score": (text_cells, nonempty_rows, populated_cells),
            }
            if best is None or candidate["score"] > best["score"]:
                best = candidate
    return best


def _union_bbox(words: Sequence[Any]) -> Optional[List[float]]:
    if not words:
        return None
    xs0 = [word.bbox[0] for word in words]
    ys0 = [word.bbox[1] for word in words]
    xs1 = [word.bbox[2] for word in words]
    ys1 = [word.bbox[3] for word in words]
    return [min(xs0), min(ys0), max(xs1), max(ys1)]


def _make_query(page: PageRecord) -> str:
    source = page.summary or first_non_empty_line(page.text) or page.text
    tokens = [token for token in tokenize(source) if token not in STOPWORDS and len(token) > 2]
    if not tokens:
        tokens = tokenize(page.text)
    if not tokens:
        return f"page {page.page_number}"
    return " ".join(tokens[:6])


def _line_candidates(page: PageRecord) -> List[str]:
    candidates: List[str] = []
    seen = set()
    sources: List[str] = []
    if page.summary:
        sources.append(page.summary)
    sources.extend(page.text.splitlines())
    for source in sources:
        clean = source.strip()
        if not clean:
            continue
        tokens = [token for token in tokenize(clean) if token not in STOPWORDS and len(token) > 2]
        if len(tokens) < 2:
            continue
        windows = [
            tokens[:6],
            tokens[2:8],
            tokens[-6:],
        ]
        for window in windows:
            if len(window) < 2:
                continue
            query = " ".join(window)
            if query not in seen:
                seen.add(query)
                candidates.append(query)
    return candidates


def _pick_search_target(env: DocEnv) -> Tuple[PageRecord, str]:
    pages = [
        page
        for page in env.document.pages
        if len(tokenize(page.text)) >= 12 or len(page.words) >= 12
    ]
    best: Optional[Tuple[Tuple[int, int, int, int], PageRecord, str]] = None
    for page in pages:
        for query in _line_candidates(page):
            results = env.search(query, top_k=3)["result"]["results"]
            returned_pages = [item["page"] for item in results]
            if page.page_number not in returned_pages:
                continue
            rank = returned_pages.index(page.page_number)
            score = (
                rank,
                page.page_number,
                abs(len(query.split()) - 4),
                -len(query),
            )
            if best is None or score < best[0]:
                best = (score, page, query)
    if best is not None:
        return best[1], best[2]
    fallback_page = _pick_primary_page(env)
    return fallback_page, _make_query(fallback_page)


def _make_text_contains(text: str) -> str:
    line = first_non_empty_line(text).strip()
    if not line:
        return ""
    if len(line) <= 60:
        return line
    return line[:60].rstrip()


def _make_claim(text: str) -> str:
    tokens = tokenize(text)
    if not tokens:
        return ""
    return " ".join(tokens[:12])


def _doc_profile(env: DocEnv) -> Dict[str, Any]:
    pages = env.document.pages
    page_count = len(pages)
    total_words = sum(len(page.words) for page in pages)
    return {
        "doc_id": env.document.doc_id,
        "title": env.document.title,
        "page_count": page_count,
        "total_words": total_words,
        "avg_words_per_page": round(total_words / page_count, 2) if page_count else 0.0,
        "table_pages": sum(1 for page in pages if page.tables),
    }


def build_call_spec(pdf_path: str) -> Dict[str, Any]:
    env = DocEnv.from_pdf(pdf_path)
    profile = _doc_profile(env)
    search_page, query = _pick_search_target(env)
    fallback_primary_page = _pick_primary_page(env)
    best_table = _pick_best_table(env)

    evidence_page = search_page.page_number
    bbox = None
    notes: List[str] = []

    if best_table is not None:
        evidence_page = best_table["page"].page_number
        bbox = list(best_table["bbox"])
    else:
        bbox = _union_bbox(search_page.words[:20]) or _union_bbox(fallback_primary_page.words[:20])
        notes.append("No reliable multi-row table detected. parse_table call omitted.")

    if bbox is None:
        bbox = [
            0.0,
            0.0,
            min(search_page.width or fallback_primary_page.width, 220.0),
            min(search_page.height or fallback_primary_page.height, 120.0),
        ]
        notes.append("Word-level bbox unavailable. Using fallback region bbox.")

    read_text = search_page.text or search_page.summary
    read_text_contains = _make_text_contains(read_text)

    crop_result = env.crop(evidence_page, bbox)
    crop_text = crop_result["result"].get("text", "") or ""
    crop_text_contains = _make_text_contains(crop_text)

    ocr_result = env.ocr(evidence_page, bbox)
    ocr_text = ocr_result["result"].get("text", "") or crop_text
    ocr_text_contains = _make_text_contains(ocr_text)

    verify_page = evidence_page
    verify_bbox = bbox
    verify_source_text = ocr_text
    if len(tokenize(verify_source_text)) < 3:
        verify_page = search_page.page_number
        verify_bbox = None
        verify_source_text = search_page.summary or search_page.text or read_text
        notes.append("Verify fallback uses whole-page evidence because region text was too short.")

    verify_claim = _make_claim(verify_source_text)
    if len(tokenize(verify_claim)) < 2:
        verify_claim = _make_claim(search_page.summary or search_page.text or read_text)
        notes.append("Generated verify claim from search-page text because region claim was too short.")

    calls: List[Dict[str, Any]] = [
        {
            "name": "overview_doc",
            "action": "overview",
            "params": {},
            "expected": {
                "status": "success",
            },
        },
        {
            "name": "search_primary_page",
            "action": "search",
            "params": {
                "query": query,
                "top_k": 3,
            },
            "expected": {
                "status": "success",
                "contains_pages": [search_page.page_number],
            },
        },
        {
            "name": "search_primary_page_cached",
            "action": "search",
            "params": {
                "query": query,
                "top_k": 3,
            },
            "expected": {
                "status": "success",
                "contains_pages": [search_page.page_number],
                "cache_hit": True,
            },
        },
        {
            "name": "read_primary_page",
            "action": "read_page",
            "params": {
                "page_ids": [search_page.page_number],
            },
            "expected": {
                "status": "success",
                "text_contains": read_text_contains,
            },
        },
        {
            "name": "crop_evidence_region",
            "action": "crop",
            "params": {
                "page_id": evidence_page,
                "bbox": bbox,
            },
            "expected": {
                "status": "success",
                "text_contains": crop_text_contains,
            },
        },
        {
            "name": "ocr_evidence_region",
            "action": "ocr",
            "params": {
                "page_id": evidence_page,
                "bbox": bbox,
            },
            "expected": {
                "status": "success",
                "text_contains": ocr_text_contains,
            },
        },
        {
            "name": "compute_sanity_check",
            "action": "compute",
            "params": {
                "expr": "(a-b)/b*100",
                "vars": {
                    "a": 3.2,
                    "b": 2.8,
                },
            },
            "expected": {
                "status": "success",
                "value_equals": 14.2857142857,
                "value_tolerance": 0.0001,
            },
        },
        {
            "name": "verify_supported_claim",
            "action": "verify",
            "params": {
                "claim": verify_claim,
                "evidence_refs": (
                    [{"page": verify_page}]
                    if verify_bbox is None
                    else [{"page": verify_page, "bbox": verify_bbox}]
                ),
            },
            "expected": {
                "status": "success",
                "support_label": "SUPPORTED",
            },
        },
        {
            "name": "detect_layout_primary_page",
            "action": "detect_layout",
            "params": {
                "page_id": search_page.page_number,
            },
            "expected": {
                "status": "success",
                "text_contains": "bbox",
            },
        },
    ]

    if best_table is not None:
        calls.insert(
            6,
            {
                "name": "parse_table_primary_table",
                "action": "parse_table",
                "params": {
                    "page_id": best_table["page"].page_number,
                    "bbox": list(best_table["bbox"]),
                },
                "expected": {
                    "status": "success",
                    "table_rows_min": 2,
                    "table_text_cells_min": 2,
                },
            },
        )

    return {
        "pdf_path": str(Path(pdf_path).resolve()),
        "generated_by": "docworldtrace.pilot.generate_call_specs",
        "doc_profile": profile,
        "notes": notes,
        "calls": calls,
    }


def write_batch(pdf_dir: str, out_dir: str) -> Dict[str, Any]:
    pdf_paths = sorted(Path(pdf_dir).glob("*.pdf"))
    if not pdf_paths:
        raise SystemExit(f"No PDFs found in {pdf_dir}")

    out_root = Path(out_dir)
    out_root.mkdir(parents=True, exist_ok=True)

    outputs = []
    for pdf_path in pdf_paths:
        payload = build_call_spec(str(pdf_path))
        out_path = out_root / f"{pdf_path.stem}.calls.json"
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        outputs.append(
            {
                "pdf": pdf_path.name,
                "call_spec": str(out_path.resolve()),
                "call_count": len(payload["calls"]),
                "notes": payload["notes"],
            }
        )

    summary = {
        "pdf_dir": str(Path(pdf_dir).resolve()),
        "out_dir": str(out_root.resolve()),
        "files": outputs,
    }
    (out_root / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate H1 call-spec drafts for PDFs.")
    parser.add_argument("--pdf-dir", default="data/raw_pdfs", help="Directory containing PDFs")
    parser.add_argument("--out-dir", default="data/calls", help="Directory to write call specs")
    args = parser.parse_args()

    summary = write_batch(args.pdf_dir, args.out_dir)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
