from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

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

NUMBER_RE = re.compile(r"-?\d+(?:,\d{3})*(?:\.\d+)?%?")
NOISY_CELL_CHARS = set("._")

DEFAULT_QUOTAS = {
    "text_lookup": 4,
    "table_lookup": 4,
    "numeric_computation": 4,
    "cross_page": 3,
    "verification": 3,
    "unanswerable": 2,
}


def _short_text(text: str, max_tokens: int = 12) -> str:
    tokens = tokenize(text)
    return " ".join(tokens[:max_tokens])


def _page_anchor(page: PageRecord) -> str:
    return page.summary or first_non_empty_line(page.text) or page.text[:120]


def _meaningful_pages(env: DocEnv) -> List[PageRecord]:
    pages = [page for page in env.document.pages if len(tokenize(page.text)) >= 8]
    pages.sort(key=lambda page: (len(tokenize(page.text)), len(page.words)), reverse=True)
    return pages


def _page_by_number(env: DocEnv, page_number: int) -> Optional[PageRecord]:
    for page in env.document.pages:
        if page.page_number == page_number:
            return page
    return None


def _parse_numeric(value: str) -> Optional[float]:
    match = NUMBER_RE.search(value.replace("$", "").replace("€", "").replace("£", ""))
    if not match:
        return None
    raw = match.group(0).replace(",", "").replace("%", "")
    try:
        return float(raw)
    except ValueError:
        return None


def _is_numericish(value: str) -> bool:
    text = str(value).strip()
    if not text or any(char.isalpha() for char in text):
        return False
    normalized = text.replace("$", "").replace("€", "").replace("£", "").replace(",", "").replace("%", "")
    try:
        float(normalized)
    except ValueError:
        return False
    return True


def _is_clean_label(value: str) -> bool:
    text = " ".join(str(value).split()).strip()
    if not text or len(text) < 2 or len(text) > 80:
        return False
    if _is_numericish(text):
        return False
    alpha_count = sum(char.isalpha() for char in text)
    if alpha_count < 2:
        return False
    noisy_count = sum(char in NOISY_CELL_CHARS for char in text)
    return noisy_count <= max(2, len(text) // 5)


def _is_clean_value(value: str) -> bool:
    text = " ".join(str(value).split()).strip()
    return bool(text) and len(text) <= 80


def _table_text_cell_count(rows: Sequence[Sequence[str]]) -> int:
    return sum(1 for row in rows for cell in row if _is_clean_label(cell))


def _table_candidates(env: DocEnv) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for page in env.document.pages:
        for table in page.tables:
            result = env.parse_table(page.page_number, table.bbox)
            rows = result.get("result", {}).get("rows", [])
            if result.get("status") != "success" or len(rows) < 2:
                continue
            nonempty_rows = [
                [str(cell).strip() for cell in row]
                for row in rows
                if any(str(cell).strip() for cell in row)
            ]
            if len(nonempty_rows) < 2:
                continue
            header = nonempty_rows[0]
            width = len(header)
            if width < 2:
                continue
            if _table_text_cell_count(nonempty_rows) < 2:
                continue
            items.append(
                {
                    "page": page,
                    "bbox": list(table.bbox),
                    "rows": nonempty_rows,
                    "header": header,
                }
            )
    return items


def _make_text_lookup_seed(doc_meta: Dict[str, Any], page: PageRecord) -> Dict[str, Any]:
    answer = _page_anchor(page)
    return {
        "seed_id": f"{doc_meta['doc_id']}__text__p{page.page_number}",
        "doc_id": doc_meta["doc_id"],
        "pdf_path": doc_meta["pdf_path"],
        "question": f"What is the heading or leading phrase on page {page.page_number}?",
        "reference_answer": answer,
        "task_type": "text_lookup",
        "difficulty": "easy",
        "required_tools": ["read_page"],
        "source": "structure_heuristic",
        "answerable": True,
        "supporting_refs": [{"page": page.page_number}],
        "metadata": {"page": page.page_number},
    }


def _make_table_lookup_seed(doc_meta: Dict[str, Any], table_item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    rows = table_item["rows"]
    header = rows[0]
    body = rows[1:]
    clean_columns = [
        (column_index, header[column_index].strip())
        for column_index in range(1, len(header))
        if _is_clean_label(header[column_index])
    ]
    if not clean_columns:
        return None
    for row in body:
        row_label = row[0].strip() if row else ""
        if not _is_clean_label(row_label):
            continue
        for column_index, column_label in clean_columns:
            if len(row) <= column_index:
                continue
            value_cell = row[column_index].strip()
            if _is_clean_value(value_cell):
                page_number = table_item["page"].page_number
                return {
                    "seed_id": f"{doc_meta['doc_id']}__table__p{page_number}",
                    "doc_id": doc_meta["doc_id"],
                    "pdf_path": doc_meta["pdf_path"],
                    "question": (
                        f'On page {page_number}, in the table, '
                        f'what is the value for row "{row_label}" under column "{column_label}"?'
                    ),
                    "reference_answer": value_cell,
                    "task_type": "table_lookup",
                    "difficulty": "medium",
                    "required_tools": ["read_page", "parse_table"],
                    "source": "structure_heuristic_v2_review",
                    "answerable": True,
                    "supporting_refs": [{"page": page_number, "bbox": table_item["bbox"]}],
                    "metadata": {
                        "page": page_number,
                        "bbox": table_item["bbox"],
                        "row_label": row_label,
                        "column_label": column_label,
                        "review_status": "needs_human_review",
                    },
                }
    return None


def _make_numeric_seed(doc_meta: Dict[str, Any], table_item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    rows = table_item["rows"]
    header = rows[0]
    body = rows[1:]
    for column_index in range(1, len(header)):
        column_label = header[column_index].strip()
        if not _is_clean_label(column_label):
            continue
        numeric_rows: List[Tuple[str, float]] = []
        for row in body:
            if len(row) <= column_index:
                continue
            numeric_value = _parse_numeric(row[column_index])
            label = row[0].strip()
            if numeric_value is not None and _is_clean_label(label):
                numeric_rows.append((label, numeric_value))
        if len(numeric_rows) >= 2:
            first_label, first_value = numeric_rows[0]
            second_label, second_value = numeric_rows[1]
            if abs(first_value) < 1e-9:
                continue
            pct = ((second_value - first_value) / abs(first_value)) * 100.0
            page_number = table_item["page"].page_number
            return {
                "seed_id": f"{doc_meta['doc_id']}__numeric__p{page_number}",
                "doc_id": doc_meta["doc_id"],
                "pdf_path": doc_meta["pdf_path"],
                "question": (
                    f'Based on the table on page {page_number}, '
                    f'for column "{column_label}", what is the percentage change '
                    f'from row "{first_label}" ({first_value:g}) to row "{second_label}" ({second_value:g})?'
                ),
                "reference_answer": f"{pct:.2f}%",
                "task_type": "numeric_computation",
                "difficulty": "medium",
                "required_tools": ["parse_table", "compute"],
                "source": "structure_heuristic_v2_review",
                "answerable": True,
                "supporting_refs": [{"page": page_number, "bbox": table_item["bbox"]}],
                "metadata": {
                    "page": page_number,
                    "bbox": table_item["bbox"],
                    "column_label": column_label,
                    "first_label": first_label,
                    "second_label": second_label,
                    "first_value": first_value,
                    "second_value": second_value,
                    "formula": "(second_value - first_value) / abs(first_value) * 100",
                    "review_status": "needs_human_review",
                },
            }
    return None


def _make_verification_seed(doc_meta: Dict[str, Any], page: PageRecord) -> Optional[Dict[str, Any]]:
    claim = _short_text(_page_anchor(page), max_tokens=10)
    if len(tokenize(claim)) < 3:
        return None
    return {
        "seed_id": f"{doc_meta['doc_id']}__verify__p{page.page_number}",
        "doc_id": doc_meta["doc_id"],
        "pdf_path": doc_meta["pdf_path"],
        "question": f'Is the following claim supported by the document: "{claim}"? Answer SUPPORTED or UNSUPPORTED.',
        "reference_answer": "SUPPORTED",
        "task_type": "verification",
        "difficulty": "medium",
        "required_tools": ["search", "read_page", "verify"],
        "source": "structure_heuristic",
        "answerable": True,
        "supporting_refs": [{"page": page.page_number}],
        "metadata": {"page": page.page_number, "claim": claim},
    }


def _make_cross_page_seed(doc_meta: Dict[str, Any], page_a: PageRecord, page_b: PageRecord) -> Optional[Dict[str, Any]]:
    anchor = _short_text(_page_anchor(page_a), max_tokens=6)
    answer = _page_anchor(page_b)
    if len(tokenize(anchor)) < 3 or len(tokenize(answer)) < 2:
        return None
    return {
        "seed_id": f"{doc_meta['doc_id']}__cross__p{page_a.page_number}_p{page_b.page_number}",
        "doc_id": doc_meta["doc_id"],
        "pdf_path": doc_meta["pdf_path"],
        "question": (
            f'First find the page about "{anchor}". What is the heading or leading phrase on the next page?'
        ),
        "reference_answer": answer,
        "task_type": "cross_page",
        "difficulty": "hard",
        "required_tools": ["search", "read_page"],
        "source": "structure_heuristic_v2_review",
        "answerable": True,
        "supporting_refs": [{"page": page_b.page_number}],
        "metadata": {
            "anchor_page": page_a.page_number,
            "answer_page": page_b.page_number,
            "anchor_phrase": anchor,
            "review_status": "needs_human_review",
        },
    }


def _make_unanswerable_seed(doc_meta: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "seed_id": f"{doc_meta['doc_id']}__refuse__generic",
        "doc_id": doc_meta["doc_id"],
        "pdf_path": doc_meta["pdf_path"],
        "question": "What is the private mobile phone number of the first author or CEO listed in the document?",
        "reference_answer": "REFUSE",
        "task_type": "unanswerable",
        "difficulty": "medium",
        "required_tools": ["search", "read_page", "refuse"],
        "source": "structure_heuristic_v2_review",
        "answerable": False,
        "supporting_refs": [],
        "metadata": {
            "review_status": "needs_human_review",
            "negative_evidence_query": "private mobile phone number first author CEO",
        },
    }


def candidate_seeds_for_env(env: DocEnv, pdf_path: str) -> List[Dict[str, Any]]:
    pdf_path_obj = Path(pdf_path)
    doc_meta = {
        "doc_id": env.document.doc_id,
        "pdf_path": str(Path("data/raw_pdfs") / pdf_path_obj.name),
    }
    pages = _meaningful_pages(env)
    if not pages:
        return []

    table_items = _table_candidates(env)
    candidates: List[Dict[str, Any]] = []
    candidates.append(_make_text_lookup_seed(doc_meta, pages[0]))

    if table_items:
        table_seed = None
        numeric_seed = None
        for table_item in table_items:
            table_seed = table_seed or _make_table_lookup_seed(doc_meta, table_item)
            numeric_seed = numeric_seed or _make_numeric_seed(doc_meta, table_item)
            if table_seed and numeric_seed:
                break
        if table_seed:
            candidates.append(table_seed)
        if numeric_seed:
            candidates.append(numeric_seed)

    verify_seed = _make_verification_seed(doc_meta, pages[min(1, len(pages) - 1)])
    if verify_seed:
        candidates.append(verify_seed)

    first_meaningful = min(pages, key=lambda page: page.page_number)
    next_page = _page_by_number(env, first_meaningful.page_number + 1)
    if next_page is not None:
        cross_seed = _make_cross_page_seed(doc_meta, first_meaningful, next_page)
        if cross_seed:
            candidates.append(cross_seed)

    candidates.append(_make_unanswerable_seed(doc_meta))
    return candidates


def write_review_markdown(seed_path: Path, seeds: Sequence[Dict[str, Any]]) -> None:
    lines = [
        "# H2 Seed Review Draft",
        "",
        "人工审查重点：question 是否无歧义，reference_answer 是否能由 supporting_refs 直接验证，unanswerable 是否确实不可回答。",
        "",
    ]
    for item in seeds:
        refs = json.dumps(item.get("supporting_refs", []), ensure_ascii=False)
        metadata = json.dumps(item.get("metadata", {}), ensure_ascii=False)
        lines.extend(
            [
                f"## {item['seed_id']}",
                "",
                f"- Type: `{item['task_type']}`",
                f"- Question: {item['question']}",
                f"- Reference: `{item['reference_answer']}`",
                f"- Required tools: `{', '.join(item['required_tools'])}`",
                f"- Supporting refs: `{refs}`",
                f"- Metadata: `{metadata}`",
                "- Human review: PASS / REVISE / DROP",
                "- Notes:",
                "",
            ]
        )
    seed_path.with_suffix(".review.md").write_text("\n".join(lines), encoding="utf-8")


def _round_robin_pick(candidates: List[Dict[str, Any]], quota: int) -> List[Dict[str, Any]]:
    by_doc: Dict[str, List[Dict[str, Any]]] = {}
    for item in candidates:
        by_doc.setdefault(item["doc_id"], []).append(item)
    for values in by_doc.values():
        values.sort(key=lambda item: item["seed_id"])

    docs = sorted(by_doc)
    picked: List[Dict[str, Any]] = []
    while len(picked) < quota and docs:
        next_docs: List[str] = []
        for doc_id in docs:
            if len(picked) >= quota:
                break
            items = by_doc[doc_id]
            if not items:
                continue
            picked.append(items.pop(0))
            if items:
                next_docs.append(doc_id)
        docs = next_docs
    return picked


def select_seed_set(candidates: List[Dict[str, Any]], quotas: Dict[str, int]) -> List[Dict[str, Any]]:
    chosen: List[Dict[str, Any]] = []
    used_ids = set()
    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for item in candidates:
        grouped.setdefault(item["task_type"], []).append(item)

    for task_type, quota in quotas.items():
        picks = _round_robin_pick(grouped.get(task_type, []), quota)
        for item in picks:
            if item["seed_id"] in used_ids:
                continue
            chosen.append(item)
            used_ids.add(item["seed_id"])

    leftovers = [item for item in candidates if item["seed_id"] not in used_ids]
    leftovers.sort(key=lambda item: (item["task_type"], item["seed_id"]))
    target_total = sum(quotas.values())
    for item in leftovers:
        if len(chosen) >= target_total:
            break
        chosen.append(item)
        used_ids.add(item["seed_id"])

    chosen.sort(key=lambda item: item["seed_id"])
    return chosen


def build_seed_file(pdf_dir: str, out_path: str, quotas: Optional[Dict[str, int]] = None) -> Dict[str, Any]:
    quotas = dict(quotas or DEFAULT_QUOTAS)
    pdf_paths = sorted(Path(pdf_dir).glob("*.pdf"))
    if not pdf_paths:
        raise SystemExit(f"No PDFs found in {pdf_dir}")

    candidates: List[Dict[str, Any]] = []
    for pdf_path in pdf_paths:
        env = DocEnv.from_pdf(str(pdf_path))
        candidates.extend(candidate_seeds_for_env(env, str(pdf_path)))

    selected = select_seed_set(candidates, quotas)
    out_file = Path(out_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as handle:
        for item in selected:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")
    write_review_markdown(out_file, selected)

    by_type: Dict[str, int] = {}
    for item in selected:
        by_type[item["task_type"]] = by_type.get(item["task_type"], 0) + 1

    summary = {
        "pdf_dir": str(Path(pdf_dir).resolve()),
        "seed_file": str(out_file.resolve()),
        "candidate_count": len(candidates),
        "selected_count": len(selected),
        "task_distribution": by_type,
        "seed_ids": [item["seed_id"] for item in selected],
    }
    summary_path = out_file.with_suffix(".summary.json")
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate H2 QA seeds from pilot PDFs.")
    parser.add_argument("--pdf-dir", default="data/raw_pdfs", help="Directory containing PDFs")
    parser.add_argument("--out", default="data/h2/seeds/pilot_seeds.jsonl", help="Output JSONL file")
    args = parser.parse_args()

    summary = build_seed_file(args.pdf_dir, args.out)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
