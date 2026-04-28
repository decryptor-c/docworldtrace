from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _round_robin(records: List[Dict[str, Any]], limit: int) -> List[Dict[str, Any]]:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for record in records:
        key = f"{record.get('task_type')}::{record.get('teacher')}"
        grouped[key].append(record)
    for items in grouped.values():
        items.sort(key=lambda item: (str(item.get("seed_id")), str(item.get("file"))))
    selected: List[Dict[str, Any]] = []
    keys = sorted(grouped)
    while len(selected) < limit and any(grouped.values()):
        for key in keys:
            if grouped[key]:
                selected.append(grouped[key].pop(0))
                if len(selected) >= limit:
                    break
    return selected


def select_sample(records: List[Dict[str, Any]], sample_size: int) -> List[Dict[str, Any]]:
    non_keep = [
        record
        for record in records
        if (record.get("docverify") or {}).get("filter_decision") != "keep"
    ]
    non_keep.sort(key=lambda item: (str(item.get("task_type")), str(item.get("teacher")), str(item.get("file"))))
    selected = non_keep[:sample_size]
    selected_files = {record["file"] for record in selected}
    remaining = [record for record in records if record["file"] not in selected_files]
    selected.extend(_round_robin(remaining, sample_size - len(selected)))
    return selected[:sample_size]


def _annotation_row(record: Dict[str, Any]) -> Dict[str, Any]:
    docverify = record.get("docverify") or {}
    return {
        "file": record.get("file"),
        "seed_id": record.get("seed_id"),
        "teacher": record.get("teacher"),
        "task_type": record.get("task_type"),
        "question": record.get("question"),
        "reference_answer": record.get("reference_answer"),
        "answerable": record.get("answerable"),
        "final_action": record.get("final_action"),
        "final_answer": record.get("final_answer"),
        "tool_sequence": record.get("tool_sequence"),
        "answer_correct_adjusted": record.get("answer_correct_adjusted"),
        "answer_match_type": record.get("answer_match_type"),
        "auto_support_label": docverify.get("support_label"),
        "auto_sufficiency": docverify.get("sufficiency"),
        "auto_filter_decision": docverify.get("filter_decision"),
        "auto_failure_taxonomy": docverify.get("failure_taxonomy"),
        "human_support_label": "",
        "human_sufficiency": "",
        "human_filter_decision": "",
        "human_tool_path_reasonable_1_to_5": "",
        "notes": "",
    }


def _write_jsonl(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")


def _write_markdown(path: Path, rows: List[Dict[str, Any]], source: str) -> None:
    lines = [
        "# H3 Natural-Distribution Manual GT Sample",
        "",
        f"- Source DocVerify review: `{source}`",
        f"- Sample count: `{len(rows)}`",
        "",
        "Labels to fill:",
        "",
        "- `human_support_label`: one of `SUPPORTED`, `PARTIAL`, `NOT_SUPPORTED`, `INSUFFICIENT`, `INVALID`",
        "- `human_sufficiency`: one of `SUFFICIENT`, `INSUFFICIENT`, `MISSING`, `INVALID`",
        "- `human_filter_decision`: one of `keep`, `review`, `reject`",
        "- `human_tool_path_reasonable_1_to_5`: integer score for tool-path reasonableness",
        "",
        "| # | Auto | Task | Teacher | Seed | Adjusted | Final | Human Notes |",
        "|---:|---|---|---|---|---:|---|---|",
    ]
    for idx, row in enumerate(rows, start=1):
        auto = f"{row['auto_filter_decision']}/{row['auto_support_label']}/{row['auto_sufficiency']}"
        final = f"{row['final_action']}: {row['final_answer']}"
        lines.append(
            "| {idx} | `{auto}` | `{task}` | `{teacher}` | `{seed}` | `{adjusted}` | `{final}` |  |".format(
                idx=idx,
                auto=auto,
                task=row["task_type"],
                teacher=row["teacher"],
                seed=row["seed_id"],
                adjusted=row["answer_correct_adjusted"],
                final=str(final).replace("|", "\\|"),
            )
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_sample(docverify: Path, out_dir: Path, sample_size: int) -> Dict[str, Any]:
    payload = _load_json(docverify)
    records = payload.get("records", [])
    sample = select_sample(records, min(sample_size, len(records)))
    rows = [_annotation_row(record) for record in sample]
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_jsonl(out_dir / "natural_manual_labels_template.jsonl", rows)
    _write_markdown(out_dir / "natural_manual_review.md", rows, str(docverify))
    summary = {
        "docverify": str(docverify),
        "sample_size_requested": sample_size,
        "sample_count": len(rows),
        "task_counts": _counts(rows, "task_type"),
        "teacher_counts": _counts(rows, "teacher"),
        "auto_filter_decisions": _counts(rows, "auto_filter_decision"),
        "outputs": {
            "jsonl": str(out_dir / "natural_manual_labels_template.jsonl"),
            "markdown": str(out_dir / "natural_manual_review.md"),
        },
    }
    _write_json(out_dir / "summary.json", summary)
    return summary


def _counts(rows: List[Dict[str, Any]], key: str) -> Dict[str, int]:
    counts: Dict[str, int] = defaultdict(int)
    for row in rows:
        counts[str(row.get(key))] += 1
    return dict(sorted(counts.items()))


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a stratified natural-distribution manual GT sample from DocVerify records.")
    parser.add_argument("--docverify", default="data/h3/docverify_plus_v5/docverify_review.json")
    parser.add_argument("--out-dir", default="data/h3/natural_gt_v5")
    parser.add_argument("--sample-size", type=int, default=100)
    args = parser.parse_args()

    summary = build_sample(Path(args.docverify), Path(args.out_dir), args.sample_size)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
