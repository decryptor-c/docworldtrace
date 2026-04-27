from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
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


@dataclass
class CheckResult:
    name: str
    status: str
    passed: bool
    detail: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "status": self.status,
            "passed": self.passed,
            "detail": self.detail,
        }


def _union_bbox(words: Sequence[Any]) -> Optional[List[float]]:
    if not words:
        return None
    xs0 = [word.bbox[0] for word in words]
    ys0 = [word.bbox[1] for word in words]
    xs1 = [word.bbox[2] for word in words]
    ys1 = [word.bbox[3] for word in words]
    return [min(xs0), min(ys0), max(xs1), max(ys1)]


def _pick_primary_page(env: DocEnv) -> PageRecord:
    pages = list(env.document.pages)
    if not pages:
        raise ValueError("document has no pages")
    ranked = sorted(
        pages,
        key=lambda page: (len(page.words), len(page.text.strip()), len(page.tables)),
        reverse=True,
    )
    return ranked[0]


def _pick_table_page(env: DocEnv) -> Optional[PageRecord]:
    pages = [page for page in env.document.pages if page.tables]
    if not pages:
        return None
    pages.sort(key=lambda page: len(page.tables), reverse=True)
    return pages[0]


def _make_query(page: PageRecord) -> str:
    source = page.summary or first_non_empty_line(page.text) or page.text
    tokens = [token for token in tokenize(source) if token not in STOPWORDS and len(token) > 2]
    if not tokens:
        tokens = tokenize(page.text)
    if not tokens:
        return f"page {page.page_number}"
    return " ".join(tokens[:6])


def _make_claim(text: str) -> str:
    tokens = tokenize(text)
    if not tokens:
        return ""
    return " ".join(tokens[:12])


def _run_check(name: str, fn) -> CheckResult:
    try:
        detail = fn()
        return CheckResult(
            name=name,
            status=detail.get("status", "success"),
            passed=bool(detail.get("passed", False)),
            detail=detail,
        )
    except Exception as exc:
        return CheckResult(
            name=name,
            status="failure",
            passed=False,
            detail={"error": str(exc)},
        )


def _doc_profile(env: DocEnv) -> Dict[str, Any]:
    pages = env.document.pages
    page_count = len(pages)
    total_words = sum(len(page.words) for page in pages)
    total_text_chars = sum(len(page.text) for page in pages)
    table_pages = sum(1 for page in pages if page.tables)
    return {
        "doc_id": env.document.doc_id,
        "title": env.document.title,
        "page_count": page_count,
        "total_words": total_words,
        "avg_words_per_page": round(total_words / page_count, 2) if page_count else 0.0,
        "total_text_chars": total_text_chars,
        "table_pages": table_pages,
        "has_text_layer": total_words > 0 or total_text_chars > 0,
    }


def evaluate_pdf(pdf_path: str) -> Dict[str, Any]:
    env = DocEnv.from_pdf(pdf_path)
    profile = _doc_profile(env)
    primary_page = _pick_primary_page(env)
    table_page = _pick_table_page(env)
    query = _make_query(primary_page)

    crop_bbox = None
    evidence_page = primary_page.page_number
    if table_page and table_page.tables:
        crop_bbox = list(table_page.tables[0].bbox)
        evidence_page = table_page.page_number
    else:
        sample_words = primary_page.words[:15]
        crop_bbox = _union_bbox(sample_words)
    if crop_bbox is None:
        crop_bbox = [0.0, 0.0, min(primary_page.width, 200.0), min(primary_page.height, 120.0)]

    checks: List[CheckResult] = []

    def overview_check() -> Dict[str, Any]:
        result = env.overview()
        return {
            "passed": result["status"] == "success" and result["result"]["page_count"] == profile["page_count"],
            "status": result["status"],
            "cache_hit": result["cache_hit"],
        }

    def read_check() -> Dict[str, Any]:
        first = env.read_page([primary_page.page_number])
        second = env.read_page([primary_page.page_number])
        text = first["result"]["pages"][0]["text"] if first["result"]["pages"] else ""
        return {
            "passed": first["status"] == "success" and second["cache_hit"] and bool(text.strip()),
            "status": first["status"],
            "cache_hit_second": second["cache_hit"],
            "page": primary_page.page_number,
            "text_chars": len(text),
        }

    def search_check() -> Dict[str, Any]:
        first = env.search(query, top_k=3)
        second = env.search(query, top_k=3)
        pages = [item["page"] for item in first["result"]["results"]]
        return {
            "passed": first["status"] in {"success", "partial"} and primary_page.page_number in pages and second["cache_hit"],
            "status": first["status"],
            "query": query,
            "returned_pages": pages,
            "target_page": primary_page.page_number,
            "cache_hit_second": second["cache_hit"],
        }

    def crop_check() -> Dict[str, Any]:
        result = env.crop(evidence_page, crop_bbox)
        text = result["result"].get("text", "")
        return {
            "passed": result["status"] in {"success", "partial"} and bool(result["result"].get("image_path") or text.strip()),
            "status": result["status"],
            "page": evidence_page,
            "bbox": crop_bbox,
            "text_chars": len(text),
            "image_path": result["result"].get("image_path"),
        }

    def ocr_check() -> Dict[str, Any]:
        first = env.ocr(evidence_page, crop_bbox)
        second = env.ocr(evidence_page, crop_bbox)
        text = first["result"].get("text", "")
        return {
            "passed": first["status"] == "success" and second["cache_hit"] and bool(text.strip()),
            "status": first["status"],
            "page": evidence_page,
            "bbox": crop_bbox,
            "text_preview": text[:200],
            "cache_hit_second": second["cache_hit"],
        }

    def layout_check() -> Dict[str, Any]:
        result = env.detect_layout(primary_page.page_number)
        elements = result["result"].get("elements", [])
        return {
            "passed": result["status"] == "success" and len(elements) > 0,
            "status": result["status"],
            "page": primary_page.page_number,
            "element_count": len(elements),
        }

    def table_check() -> Dict[str, Any]:
        if not table_page or not table_page.tables:
            return {
                "passed": False,
                "status": "skipped",
                "reason": "no_table_detected",
            }
        first = env.parse_table(table_page.page_number, table_page.tables[0].bbox)
        second = env.parse_table(table_page.page_number, table_page.tables[0].bbox)
        rows = first["result"].get("rows", [])
        return {
            "passed": first["status"] == "success" and second["cache_hit"] and len(rows) >= 2,
            "status": first["status"],
            "page": table_page.page_number,
            "row_count": len(rows),
            "cache_hit_second": second["cache_hit"],
        }

    def compute_check() -> Dict[str, Any]:
        result = env.compute("(a-b)/b*100", {"a": 3.2, "b": 2.8})
        value = result["result"].get("value")
        passed = result["status"] == "success" and isinstance(value, (int, float)) and abs(value - 14.2857142857) < 1e-4
        return {
            "passed": passed,
            "status": result["status"],
            "value": value,
        }

    def verify_check() -> Dict[str, Any]:
        ocr = env.ocr(evidence_page, crop_bbox)
        claim = _make_claim(ocr["result"].get("text", "") or primary_page.summary or primary_page.text)
        if not claim:
            return {
                "passed": False,
                "status": "skipped",
                "reason": "empty_claim",
            }
        first = env.verify(claim, [{"page": evidence_page, "bbox": crop_bbox}])
        second = env.verify(claim, [{"page": evidence_page, "bbox": crop_bbox}])
        return {
            "passed": first["status"] == "success" and first["result"].get("label") == "SUPPORTED" and second["cache_hit"],
            "status": first["status"],
            "claim": claim,
            "label": first["result"].get("label"),
            "sufficiency": first["result"].get("sufficiency"),
            "cache_hit_second": second["cache_hit"],
        }

    checks.append(_run_check("overview", overview_check))
    checks.append(_run_check("read_page", read_check))
    checks.append(_run_check("search", search_check))
    checks.append(_run_check("crop", crop_check))
    checks.append(_run_check("ocr", ocr_check))
    checks.append(_run_check("detect_layout", layout_check))
    checks.append(_run_check("parse_table", table_check))
    checks.append(_run_check("compute", compute_check))
    checks.append(_run_check("verify", verify_check))

    attempted = [check for check in checks if check.status != "skipped"]
    passed = [check for check in attempted if check.passed]
    skipped = [check for check in checks if check.status == "skipped"]
    cache_checks = [
        check
        for check in checks
        if check.detail.get("cache_hit_second") is not None
    ]
    cache_passed = [
        check
        for check in cache_checks
        if check.detail.get("cache_hit_second") is True
    ]

    pass_rate = len(passed) / len(attempted) if attempted else 0.0
    cache_rate = len(cache_passed) / len(cache_checks) if cache_checks else 0.0

    suitability = "high"
    reasons = []
    if not profile["has_text_layer"]:
        suitability = "low"
        reasons.append("text_layer_missing")
    if profile["page_count"] > 120:
        suitability = "medium" if suitability == "high" else suitability
        reasons.append("very_long_document")
    if any(check.name == "ocr" and not check.passed for check in checks):
        suitability = "medium" if suitability == "high" else suitability
        reasons.append("ocr_risk")
    if any(check.name == "parse_table" and check.status == "failure" for check in checks):
        suitability = "medium" if suitability == "high" else suitability
        reasons.append("table_parse_risk")
    if pass_rate < 0.75:
        suitability = "low"
        reasons.append("low_tool_pass_rate")

    recommended = suitability in {"high", "medium"}
    return {
        "pdf_path": str(Path(pdf_path).resolve()),
        "profile": profile,
        "checks": [check.to_dict() for check in checks],
        "metrics": {
            "attempted_checks": len(attempted),
            "passed_checks": len(passed),
            "skipped_checks": len(skipped),
            "pass_rate": round(pass_rate, 4),
            "cache_check_count": len(cache_checks),
            "cache_pass_rate": round(cache_rate, 4),
        },
        "suitability": suitability,
        "recommended_for_h1": recommended,
        "reasons": reasons,
    }


def _write_markdown(path: Path, payload: Dict[str, Any]) -> None:
    profile = payload["profile"]
    metrics = payload["metrics"]
    lines = [
        f"# Auto H1 Evaluation: {Path(payload['pdf_path']).name}",
        "",
        f"- Suitability: `{payload['suitability']}`",
        f"- Recommended for H1: `{payload['recommended_for_h1']}`",
        f"- Page count: `{profile['page_count']}`",
        f"- Avg words/page: `{profile['avg_words_per_page']}`",
        f"- Table pages: `{profile['table_pages']}`",
        f"- Pass rate: `{metrics['pass_rate']:.2%}`",
        f"- Cache pass rate: `{metrics['cache_pass_rate']:.2%}`",
        "",
        "## Checks",
        "",
    ]
    for check in payload["checks"]:
        lines.append(
            f"- `{check['name']}`: "
            f"{'PASS' if check['passed'] else check['status'].upper()}"
        )
    lines.append("")
    if payload["reasons"]:
        lines.append("## Notes")
        lines.append("")
        for reason in payload["reasons"]:
            lines.append(f"- `{reason}`")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def run_batch(pdf_dir: str, out_dir: str) -> Dict[str, Any]:
    pdf_paths = sorted(Path(pdf_dir).glob("*.pdf"))
    if not pdf_paths:
        raise SystemExit(f"No PDFs found in {pdf_dir}")

    out_root = Path(out_dir)
    out_root.mkdir(parents=True, exist_ok=True)

    documents = []
    for pdf_path in pdf_paths:
        payload = evaluate_pdf(str(pdf_path))
        stem = pdf_path.stem
        json_path = out_root / f"{stem}.json"
        md_path = out_root / f"{stem}.md"
        json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        _write_markdown(md_path, payload)
        documents.append(payload)

    high = sum(1 for doc in documents if doc["suitability"] == "high")
    medium = sum(1 for doc in documents if doc["suitability"] == "medium")
    low = sum(1 for doc in documents if doc["suitability"] == "low")
    recommended = [Path(doc["pdf_path"]).name for doc in documents if doc["recommended_for_h1"]]

    summary = {
        "pdf_dir": str(Path(pdf_dir).resolve()),
        "document_count": len(documents),
        "high": high,
        "medium": medium,
        "low": low,
        "recommended_for_h1": recommended,
        "documents": documents,
    }
    summary_path = out_root / "summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Auto-evaluate PDFs for Pilot Exp-1 / H1.")
    parser.add_argument("--pdf-dir", default="data/raw_pdfs", help="Directory containing PDFs")
    parser.add_argument(
        "--out-dir",
        default="data/reports/rawdata_eval",
        help="Directory for JSON/Markdown reports",
    )
    args = parser.parse_args()

    summary = run_batch(args.pdf_dir, args.out_dir)
    print(json.dumps(
        {
            "document_count": summary["document_count"],
            "high": summary["high"],
            "medium": summary["medium"],
            "low": summary["low"],
            "recommended_for_h1": summary["recommended_for_h1"],
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
