#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List


TERMINAL_ACTIONS = {"answer", "refuse"}
EVIDENCE_TOOLS = {"overview", "search", "read_page", "crop", "ocr", "parse_table", "compute", "verify"}


def _pct(numerator: int, denominator: int) -> float:
    return round(numerator / denominator, 4) if denominator else 0.0


def _observation_success(step: Dict[str, Any]) -> bool:
    return (step.get("observation") or {}).get("status") == "success"


def _any_evidence_success(payload: Dict[str, Any]) -> bool:
    return any(
        step.get("action") in EVIDENCE_TOOLS and _observation_success(step)
        for step in payload.get("trajectory", [])
    )


def _tool_success(payload: Dict[str, Any], tool: str) -> bool:
    return any(step.get("action") == tool and _observation_success(step) for step in payload.get("trajectory", []))


def _expected_terminal(seed: Dict[str, Any]) -> str:
    return "answer" if seed.get("answerable", True) else "refuse"


def _contains_subsequence(sequence: List[str], expected: List[str]) -> bool:
    index = 0
    for action in sequence:
        if index < len(expected) and action == expected[index]:
            index += 1
    return index == len(expected)


def _acceptable_path_ok(payload: Dict[str, Any], evidence_path_ok: bool) -> bool:
    seed = payload["seed"]
    paths = seed.get("acceptable_paths") or []
    if not paths:
        return evidence_path_ok
    sequence = payload.get("tool_sequence", [])
    return any(_contains_subsequence(sequence, path) for path in paths)


def _score_payload(path: Path, payload: Dict[str, Any]) -> Dict[str, Any]:
    seed = payload["seed"]
    sequence = payload.get("tool_sequence", [])
    required = [tool for tool in seed.get("required_tools", []) if tool not in TERMINAL_ACTIONS]
    missing = [tool for tool in required if tool not in sequence]
    failed_required = [tool for tool in required if tool in sequence and not _tool_success(payload, tool)]
    terminal_ok = payload.get("final_action") == _expected_terminal(seed)
    nonterminal_used = any(tool not in TERMINAL_ACTIONS for tool in sequence)
    evidence_success = _any_evidence_success(payload)
    strict_path_ok = (
        payload.get("status") == "completed"
        and terminal_ok
        and not missing
        and not failed_required
        and evidence_success
    )
    evidence_path_ok = (
        payload.get("status") == "completed"
        and terminal_ok
        and nonterminal_used
        and evidence_success
    )
    acceptable_path_ok = (
        payload.get("status") == "completed"
        and terminal_ok
        and evidence_success
        and _acceptable_path_ok(payload, evidence_path_ok)
    )

    if strict_path_ok:
        strict_issue = "path_ok"
    elif payload.get("status") == "format_error":
        strict_issue = "format_error"
    elif payload.get("status") == "budget_exhausted":
        strict_issue = "budget_exhausted"
    elif not terminal_ok:
        strict_issue = "wrong_terminal"
    elif missing:
        strict_issue = "missing_required_tool"
    elif failed_required:
        strict_issue = "required_tool_no_success_observation"
    else:
        strict_issue = "no_successful_evidence_observation"

    if acceptable_path_ok:
        acceptable_issue = "acceptable_path_ok"
    elif payload.get("status") == "format_error":
        acceptable_issue = "format_error"
    elif payload.get("status") == "budget_exhausted":
        acceptable_issue = "budget_exhausted"
    elif not terminal_ok:
        acceptable_issue = "wrong_terminal"
    elif not nonterminal_used:
        acceptable_issue = "direct_terminal"
    elif not evidence_success:
        acceptable_issue = "no_successful_evidence_observation"
    else:
        acceptable_issue = "tool_path_not_acceptable"

    return {
        "file": str(path),
        "teacher": payload.get("teacher", {}).get("name"),
        "seed_id": seed.get("seed_id"),
        "task_type": seed.get("task_type"),
        "status": payload.get("status"),
        "tool_sequence": sequence,
        "final_action": payload.get("final_action"),
        "expected_terminal": _expected_terminal(seed),
        "strict_path_ok": strict_path_ok,
        "evidence_path_ok": evidence_path_ok,
        "acceptable_path_ok": acceptable_path_ok,
        "terminal_ok": terminal_ok,
        "nonterminal_used": nonterminal_used,
        "required_tool_covered": not missing,
        "missing_required_tools": missing,
        "failed_required_tools": failed_required,
        "any_evidence_success": evidence_success,
        "strict_path_issue": strict_issue,
        "acceptable_path_issue": acceptable_issue,
    }


def _summarize(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    total = len(records)
    return {
        "count": total,
        "strict_path_ok_rate": _pct(sum(record["strict_path_ok"] for record in records), total),
        "evidence_path_ok_rate": _pct(sum(record["evidence_path_ok"] for record in records), total),
        "acceptable_path_ok_rate": _pct(sum(record["acceptable_path_ok"] for record in records), total),
        "proper_termination_rate": _pct(
            sum(record["status"] == "completed" and record["final_action"] in TERMINAL_ACTIONS for record in records),
            total,
        ),
        "expected_terminal_rate": _pct(sum(record["terminal_ok"] for record in records), total),
        "nonterminal_tool_use_rate": _pct(sum(record["nonterminal_used"] for record in records), total),
        "required_tool_coverage_rate": _pct(sum(record["required_tool_covered"] for record in records), total),
        "successful_evidence_observation_rate": _pct(sum(record["any_evidence_success"] for record in records), total),
        "strict_path_issues": dict(Counter(record["strict_path_issue"] for record in records)),
        "acceptable_path_issues": dict(Counter(record["acceptable_path_issue"] for record in records)),
    }


def evaluate(rollout_dir: Path) -> Dict[str, Any]:
    files = sorted(rollout_dir.glob("*/*.json"))
    records = [_score_payload(path, json.loads(path.read_text(encoding="utf-8"))) for path in files]
    by_teacher = defaultdict(list)
    by_task = defaultdict(list)
    for record in records:
        by_teacher[record["teacher"]].append(record)
        by_task[record["task_type"]].append(record)
    return {
        "rollout_dir": str(rollout_dir),
        "overall": _summarize(records),
        "by_teacher": {key: _summarize(items) for key, items in sorted(by_teacher.items())},
        "by_task_type": {key: _summarize(items) for key, items in sorted(by_task.items())},
        "records": records,
    }


def write_markdown(path: Path, payload: Dict[str, Any]) -> None:
    lines = [
        "# H2 Path Review",
        "",
        f"- Rollout dir: `{payload['rollout_dir']}`",
        "",
        "## Overall",
        "",
    ]
    for key, value in payload["overall"].items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## By Teacher", ""])
    for key, stats in payload["by_teacher"].items():
        lines.append(f"### {key}")
        for stat_key, value in stats.items():
            lines.append(f"- {stat_key}: `{value}`")
        lines.append("")
    lines.extend(["## By Task Type", ""])
    for key, stats in payload["by_task_type"].items():
        lines.append(f"### {key}")
        for stat_key, value in stats.items():
            lines.append(f"- {stat_key}: `{value}`")
        lines.append("")
    lines.extend(["## Non-Acceptable Path Cases", ""])
    for record in payload["records"]:
        if record["acceptable_path_ok"]:
            continue
        lines.append(f"### {record['acceptable_path_issue']} | {record['teacher']} | {record['seed_id']}")
        lines.append(f"- file: `{record['file']}`")
        lines.append(f"- task: `{record['task_type']}`")
        lines.append(f"- sequence: `{record['tool_sequence']}`")
        lines.append(f"- final action: `{record['final_action']}`, expected: `{record['expected_terminal']}`")
        lines.append(f"- missing required: `{record['missing_required_tools']}`")
        lines.append(f"- failed required: `{record['failed_required_tools']}`")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Review H2 rollout paths independently from answer scoring.")
    parser.add_argument("rollout_dir")
    parser.add_argument("out_dir")
    args = parser.parse_args()

    payload = evaluate(Path(args.rollout_dir))
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "path_review.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(out_dir / "path_review.md", payload)
    print(json.dumps(payload["overall"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
