from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, pstdev
from typing import Any, Dict, List, Optional, Tuple

from .h2_rollout import display_path


ALL_ACTIONS = [
    "overview",
    "search",
    "read_page",
    "crop",
    "ocr",
    "parse_table",
    "compute",
    "verify",
    "answer",
    "refuse",
]

CORE_PILOT_ACTIONS = {"search", "read_page", "parse_table", "compute", "verify", "answer", "refuse"}


def _pct(numerator: int, denominator: int) -> float:
    return round(numerator / denominator, 4) if denominator else 0.0


def _sequence_key(sequence: List[str]) -> str:
    return " -> ".join(sequence) if sequence else "<empty>"


def _load_docverify(path: Optional[str]) -> Dict[str, Dict[str, Any]]:
    if not path:
        return {}
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    payload = json.loads(path_obj.read_text(encoding="utf-8"))
    return {record["file"]: record for record in payload.get("records", [])}


def _search_queries(payload: Dict[str, Any]) -> List[str]:
    queries = []
    for step in payload.get("trajectory", []):
        if step.get("action") != "search":
            continue
        action_input = step.get("action_input") or {}
        query = str(action_input.get("query", "")).strip()
        if query:
            queries.append(query)
    return queries


def _normalized_query(query: str) -> str:
    return " ".join(query.lower().split())


def _collect_records(rollout_dir: Path, docverify_by_file: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for path in sorted(rollout_dir.glob("*/*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        display = display_path(str(path))
        seed = payload["seed"]
        sequence = [action for action in payload.get("tool_sequence", []) if action]
        docverify = docverify_by_file.get(display) or docverify_by_file.get(str(path)) or {}
        filter_decision = (docverify.get("docverify") or {}).get("filter_decision")
        support_label = (docverify.get("docverify") or {}).get("support_label")
        records.append(
            {
                "file": display,
                "teacher": payload.get("teacher", {}).get("name"),
                "seed_id": seed.get("seed_id"),
                "task_type": seed.get("task_type"),
                "status": payload.get("status"),
                "sequence": sequence,
                "sequence_key": _sequence_key(sequence),
                "step_count": len(sequence),
                "actions": sorted(set(sequence)),
                "search_queries": _search_queries(payload),
                "docverify_filter_decision": filter_decision,
                "docverify_support_label": support_label,
            }
        )
    return records


def _summarize(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    total = len(records)
    unique_sequences = Counter(record["sequence_key"] for record in records)
    action_counts = Counter(action for record in records for action in record["sequence"])
    action_coverage = sorted(action for action in ALL_ACTIONS if action_counts[action] > 0)
    core_coverage = sorted(action for action in CORE_PILOT_ACTIONS if action_counts[action] > 0)
    step_counts = [record["step_count"] for record in records]
    queries = [query for record in records for query in record["search_queries"]]
    normalized_queries = [_normalized_query(query) for query in queries]
    unique_queries = sorted(set(normalized_queries))
    seed_query_pairs = {
        (record["seed_id"], _normalized_query(query))
        for record in records
        for query in record["search_queries"]
    }
    seeds_with_search = {record["seed_id"] for record in records if record["search_queries"]}
    unique_seed_query_pair_count = len(seed_query_pairs)
    return {
        "count": total,
        "unique_sequence_count": len(unique_sequences),
        "unique_sequence_ratio": _pct(len(unique_sequences), total),
        "top_sequences": dict(unique_sequences.most_common(20)),
        "action_coverage_count": len(action_coverage),
        "action_coverage": action_coverage,
        "core_pilot_action_coverage_count": len(core_coverage),
        "core_pilot_action_coverage": core_coverage,
        "action_counts": dict(action_counts),
        "step_count_mean": round(mean(step_counts), 4) if step_counts else 0.0,
        "step_count_std": round(pstdev(step_counts), 4) if len(step_counts) > 1 else 0.0,
        "step_count_distribution": dict(Counter(step_counts)),
        "search_call_count": len(queries),
        "unique_search_query_count": len(unique_queries),
        "unique_search_query_ratio": _pct(len(unique_queries), len(queries)),
        "seeds_with_search_count": len(seeds_with_search),
        "unique_seed_query_pair_count": unique_seed_query_pair_count,
        "unique_seed_query_pair_ratio": _pct(unique_seed_query_pair_count, len(queries)),
        "search_query_counts": dict(Counter(normalized_queries).most_common(30)),
    }


def _by_key(records: List[Dict[str, Any]], key: str) -> Dict[str, Dict[str, Any]]:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[str(record.get(key))].append(record)
    return {name: _summarize(items) for name, items in sorted(grouped.items())}


def _path_cross_table(records: List[Dict[str, Any]]) -> Dict[str, Dict[str, int]]:
    table: Dict[str, Counter] = defaultdict(Counter)
    for record in records:
        table[record["task_type"]][record["sequence_key"]] += 1
    return {task: dict(counter.most_common()) for task, counter in sorted(table.items())}


def _kept_records(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    with_docverify = [record for record in records if record.get("docverify_filter_decision")]
    if not with_docverify:
        return []
    return [record for record in records if record.get("docverify_filter_decision") == "keep"]


def _h4_lite_decision(overall: Dict[str, Any], by_task_type: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    covered_tasks = {task for task, stats in by_task_type.items() if stats["count"] > 0}
    expected_tasks = {"text_lookup", "table_lookup", "numeric_computation", "cross_page", "verification", "unanswerable"}
    task_coverage_ok = expected_tasks.issubset(covered_tasks)
    core_action_ok = CORE_PILOT_ACTIONS.issubset(set(overall["core_pilot_action_coverage"]))
    sequence_ok = overall["unique_sequence_count"] >= 6
    query_ok = (
        overall["search_call_count"] == 0
        or overall["unique_seed_query_pair_ratio"] >= 0.5
    )
    passed = task_coverage_ok and core_action_ok and sequence_ok and query_ok
    return {
        "h4_lite_passed": passed,
        "task_coverage_ok": task_coverage_ok,
        "core_action_coverage_ok": core_action_ok,
        "sequence_diversity_ok": sequence_ok,
        "search_query_diversity_ok": query_ok,
        "covered_tasks": sorted(covered_tasks),
        "expected_tasks": sorted(expected_tasks),
        "rationale": (
            "H4-lite passes when six task types are covered, core pilot actions are used, "
            "at least six unique tool sequences appear, and seed-level search queries are not highly duplicated."
        ),
    }


def evaluate(rollout_dir: Path, docverify_path: Optional[str]) -> Dict[str, Any]:
    docverify_by_file = _load_docverify(docverify_path)
    records = _collect_records(rollout_dir, docverify_by_file)
    kept = _kept_records(records)
    overall = _summarize(records)
    by_task_type = _by_key(records, "task_type")
    payload = {
        "rollout_dir": display_path(str(rollout_dir)),
        "docverify_path": display_path(docverify_path) if docverify_path else None,
        "overall": overall,
        "by_teacher": _by_key(records, "teacher"),
        "by_task_type": by_task_type,
        "task_type_path_table": _path_cross_table(records),
        "kept_only": _summarize(kept) if kept else None,
        "h4_lite_decision": _h4_lite_decision(overall, by_task_type),
        "records": records,
    }
    return payload


def write_markdown(path: Path, payload: Dict[str, Any]) -> None:
    overall = payload["overall"]
    decision = payload["h4_lite_decision"]
    lines = [
        "# H4 Trajectory Diversity Analysis",
        "",
        f"- Rollout dir: `{payload['rollout_dir']}`",
        f"- DocVerify++ input: `{payload['docverify_path']}`",
        f"- H4-lite passed: `{decision['h4_lite_passed']}`",
        "",
        "## Overall",
        "",
        f"- Count: `{overall['count']}`",
        f"- Unique sequence count: `{overall['unique_sequence_count']}`",
        f"- Unique sequence ratio: `{overall['unique_sequence_ratio']:.2%}`",
        f"- Action coverage: `{overall['action_coverage_count']}/10` `{overall['action_coverage']}`",
        f"- Core pilot action coverage: `{overall['core_pilot_action_coverage_count']}/7` `{overall['core_pilot_action_coverage']}`",
        f"- Step count mean/std: `{overall['step_count_mean']}` / `{overall['step_count_std']}`",
        f"- Step count distribution: `{overall['step_count_distribution']}`",
        f"- Search calls: `{overall['search_call_count']}`",
        f"- Unique search query count: `{overall['unique_search_query_count']}`",
        f"- Unique search query ratio: `{overall['unique_search_query_ratio']:.2%}`",
        f"- Seeds with search: `{overall['seeds_with_search_count']}`",
        f"- Unique seed-query pair count: `{overall['unique_seed_query_pair_count']}`",
        f"- Unique seed-query pair ratio: `{overall['unique_seed_query_pair_ratio']:.2%}`",
        "",
        "## H4-Lite Decision",
        "",
    ]
    for key, value in decision.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## Top Tool Sequences", ""])
    for sequence, count in overall["top_sequences"].items():
        lines.append(f"- `{sequence}`: `{count}`")
    lines.extend(["", "## By Task Type", ""])
    for task_type, stats in payload["by_task_type"].items():
        lines.append(f"### {task_type}")
        lines.append(f"- Count: `{stats['count']}`")
        lines.append(f"- Unique sequence count: `{stats['unique_sequence_count']}`")
        lines.append(f"- Step mean/std: `{stats['step_count_mean']}` / `{stats['step_count_std']}`")
        lines.append(f"- Action coverage: `{stats['action_coverage']}`")
        lines.append("- Paths:")
        for sequence, count in payload["task_type_path_table"][task_type].items():
            lines.append(f"  - `{sequence}`: `{count}`")
        lines.append("")
    if payload.get("kept_only"):
        kept = payload["kept_only"]
        lines.extend(
            [
                "## Kept Trajectories Only",
                "",
                f"- Count: `{kept['count']}`",
                f"- Unique sequence count: `{kept['unique_sequence_count']}`",
                f"- Unique sequence ratio: `{kept['unique_sequence_ratio']:.2%}`",
                f"- Action coverage: `{kept['action_coverage_count']}/10` `{kept['action_coverage']}`",
                "",
            ]
        )
    lines.extend(
        [
            "## Interpretation",
            "",
            "H4 evaluates whether supported trajectories are diverse enough to serve as process data rather than repeated answer-only templates.",
            "For the current pilot, the strict original threshold of unique_sequence_ratio >= 50% may be too high because each seed is repeated across two teachers and two runs. H4-lite therefore emphasizes task coverage, core action coverage, and task-specific path separation.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze H4 trajectory diversity.")
    parser.add_argument("--rollout-dir", default="data/h2/rollouts_v4")
    parser.add_argument("--docverify", default=None, help="Optional DocVerify++ review JSON")
    parser.add_argument("--out-dir", default="data/h4/diversity_v4")
    args = parser.parse_args()

    payload = evaluate(Path(args.rollout_dir), args.docverify)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "diversity_report.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(out_dir / "diversity_report.md", payload)
    print(json.dumps(payload["h4_lite_decision"], ensure_ascii=False, indent=2))
    print(f"H4 diversity report written to {out_dir}")


if __name__ == "__main__":
    main()
