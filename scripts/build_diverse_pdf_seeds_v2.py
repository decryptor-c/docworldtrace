#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Iterable, List


DEFAULT_IN = Path("data/h2/seeds/diverse_pdf_seeds_v1_corrected.jsonl")
DEFAULT_OUT = Path("data/h2/seeds/diverse_pdf_seeds_v2.jsonl")
DEFAULT_REVIEW = Path("data/h2/seeds/diverse_pdf_seeds_v2.review.md")


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, records: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(record, ensure_ascii=False, sort_keys=True) for record in records]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _first_ref(seed: Dict[str, Any]) -> Dict[str, Any]:
    refs = seed.get("supporting_refs") or []
    return refs[0] if refs and isinstance(refs[0], dict) else {}


def _target_page(seed: Dict[str, Any]) -> int | None:
    page = seed.get("metadata", {}).get("page")
    if page is None:
        page = _first_ref(seed).get("page")
    return page


def _bbox(seed: Dict[str, Any]) -> List[float] | None:
    bbox = seed.get("metadata", {}).get("bbox")
    if bbox is None:
        bbox = _first_ref(seed).get("bbox")
    return bbox if isinstance(bbox, list) and len(bbox) == 4 else None


def append_audit(seed: Dict[str, Any], note: str) -> None:
    metadata = seed.setdefault("metadata", {})
    old_note = metadata.get("audit_note")
    metadata["audit_note"] = f"{old_note} | V2 fix: {note}" if old_note else f"V2 fix: {note}"


def add_default_paths_and_hints(seed: Dict[str, Any]) -> None:
    task_type = seed.get("task_type")
    page = _target_page(seed)
    bbox = _bbox(seed)
    hints = deepcopy(seed.get("tool_hints") or {})
    if page is not None:
        hints.setdefault("target_page", page)
    if bbox is not None and task_type in {"table_lookup", "numeric_computation"}:
        hints.setdefault("table_bbox_hint", bbox)
        hints.setdefault("bbox_note", "Use this bbox as the first parse_table/crop region; it covers the relevant table.")
    if task_type == "table_lookup":
        seed.setdefault("acceptable_paths", [["read_page", "parse_table", "answer"], ["parse_table", "answer"], ["read_page", "ocr", "answer"]])
        hints.setdefault("preferred_first_tool", "parse_table" if bbox is not None else "read_page")
    elif task_type == "numeric_computation":
        seed.setdefault("acceptable_paths", [["parse_table", "compute", "answer"], ["read_page", "parse_table", "compute", "answer"], ["ocr", "compute", "answer"]])
        hints.setdefault("preferred_first_tool", "parse_table" if bbox is not None else "read_page")
        hints.setdefault("compute_note", "Use the numeric formula in the question and preserve the sign of the percentage change.")
    elif task_type == "unanswerable":
        seed.setdefault("acceptable_paths", [["search", "read_page", "refuse"], ["search", "search", "refuse"]])
    elif task_type == "verification":
        seed.setdefault("acceptable_paths", [["search", "read_page", "verify", "answer"], ["read_page", "verify", "answer"], ["read_page", "answer"]])
    elif task_type == "cross_page":
        seed.setdefault("acceptable_paths", [["search", "read_page", "answer"]])
    elif task_type == "text_lookup":
        seed.setdefault("acceptable_paths", [["read_page", "answer"], ["search", "read_page", "answer"]])
    if hints:
        seed["tool_hints"] = hints


def fix_seed(seed: Dict[str, Any]) -> List[str]:
    seed_id = seed["seed_id"]
    notes: List[str] = []
    if seed_id == "epa_ghg_inventory_1990_2022__numeric__p41":
        seed["reference_answer"] = "-14.94%"
        append_audit(seed, "Corrected the two-decimal signed percentage GT from -14.93% to -14.94%.")
        notes.append("GT -14.93% -> -14.94%.")
    elif seed_id == "nasa_fy2025_budget_summary__numeric__p4":
        seed["question"] = (
            "Based on the table on page 4, in column \"FY 2023 Operating Plan\", compute the signed percentage change "
            "from row \"Deep Space Exploration Systems\" (7447.6) to row \"Space Operations\" (4266.7), using "
            "(Space Operations - Deep Space Exploration Systems) / abs(Deep Space Exploration Systems) * 100. "
            "Report only the final signed percentage with two decimals."
        )
        append_audit(seed, "Removed the ambiguous 'is less than' phrasing and made the signed formula explicit.")
        notes.append("Query now makes the negative sign explicit.")
    elif seed_id == "scotus_loper_bright_2024__text__p2":
        seed["question"] = (
            "On page 2, ignore the running page header line \"2 LOPER BRIGHT ENTERPRISES v. RAIMONDO\". "
            "What section heading appears immediately below that header? Return only the heading."
        )
        append_audit(seed, "Disambiguated the target heading from the running page header.")
        notes.append("Query now excludes the running page header.")
    elif seed_id == "usgs_mcs_2025__text__p21":
        seed["question"] = (
            "On page 21, ignore page numbers and footnote markers. What table caption begins the page? "
            "Return the caption text only."
        )
        append_audit(seed, "Disambiguated the caption from the visible page number.")
        notes.append("Query now excludes page numbers.")
    elif seed_id == "nasa_fy2025_budget_summary__cross__p2_p3":
        seed["question"] = (
            "Use search to find the page about \"international space station while partnering with U.S. industry\". "
            "Then inspect the following page and report only the first three words of the first bullet."
        )
        seed["reference_answer"] = "Drives scientific discovery"
        append_audit(seed, "Aligned the query with a short leading-phrase GT instead of a long bullet clause.")
        notes.append("GT shortened to first three words.")
    elif seed_id == "2310.03302v2__cross__p1_p2":
        seed["question"] = (
            "Use search to find the page about \"mlagentbench evaluating language agents on\". "
            "Then inspect the following page and report the running paper title printed at the very top of that page. "
            "Ignore figure captions such as \"Starter Files\"."
        )
        append_audit(seed, "Clarified that the desired next-page phrase is the running title, not the first figure caption.")
        notes.append("Query now excludes figure captions.")
    elif seed_id == "ipcc_ar6_syr_longer_report__table__p11":
        seed["seed_id"] = "ipcc_ar6_syr_longer_report__text__p11"
        seed["question"] = "On page 11, what section heading appears at the top of the page? Return only the heading."
        seed["reference_answer"] = "Current Status and Trends"
        seed["task_type"] = "text_lookup"
        seed["difficulty"] = "easy"
        seed["required_tools"] = ["read_page"]
        seed["supporting_refs"] = [{"page": 11}]
        seed["metadata"] = {
            "page": 11,
            "review_status": "needs_human_review",
            "previous_seed_id": seed_id,
            "previous_task_type": "table_lookup",
            "audit_note": "V2 fix: page 11 is figure-like in DocEnv and not a reliable table extraction target; converted to stable text_lookup.",
        }
        notes.append("Converted unreliable IPCC table seed to text_lookup.")
    add_default_paths_and_hints(seed)
    return notes


def write_review(path: Path, seeds: List[Dict[str, Any]], changes: Dict[str, List[str]]) -> None:
    lines = [
        "# Diverse PDF Seeds V2 Review",
        "",
        f"- Seed count: `{len(seeds)}`",
        "- Source: `data/h2/seeds/diverse_pdf_seeds_v1_corrected.jsonl`",
        "- Output: `data/h2/seeds/diverse_pdf_seeds_v2.jsonl`",
        "",
        "## V2 Fixes",
        "",
    ]
    for seed_id, notes in changes.items():
        lines.append(f"### {seed_id}")
        for note in notes:
            lines.append(f"- {note}")
        lines.append("")
    lines.extend(["## Seeds", ""])
    for index, seed in enumerate(seeds, start=1):
        lines.append(f"### {index}. `{seed['seed_id']}`")
        lines.append(f"- doc_id: `{seed['doc_id']}`")
        lines.append(f"- task_type: `{seed['task_type']}`")
        lines.append(f"- question: {seed['question']}")
        lines.append(f"- reference_answer: `{seed['reference_answer']}`")
        lines.append(f"- required_tools: `{seed.get('required_tools', [])}`")
        if seed.get("tool_hints"):
            lines.append(f"- tool_hints: `{json.dumps(seed['tool_hints'], ensure_ascii=False)}`")
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build V2 diverse-PDF seeds with audited fixes.")
    parser.add_argument("--input", default=str(DEFAULT_IN))
    parser.add_argument("--output", default=str(DEFAULT_OUT))
    parser.add_argument("--review", default=str(DEFAULT_REVIEW))
    args = parser.parse_args()

    seeds = load_jsonl(Path(args.input))
    changes: Dict[str, List[str]] = {}
    seen = set()
    for seed in seeds:
        original_id = seed["seed_id"]
        notes = fix_seed(seed)
        if notes:
            changes[original_id] = notes
        if seed["seed_id"] in seen:
            raise SystemExit(f"Duplicate seed_id after V2 fixes: {seed['seed_id']}")
        seen.add(seed["seed_id"])
    write_jsonl(Path(args.output), seeds)
    write_review(Path(args.review), seeds, changes)
    print(json.dumps({"input": args.input, "output": args.output, "review": args.review, "seed_count": len(seeds), "changed": changes}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
