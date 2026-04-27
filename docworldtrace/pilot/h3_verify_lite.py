from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional

from .h2_eval import _score_rollout
from .h2_rollout import display_path


TERMINAL_ACTIONS = {"answer", "refuse"}
DOCUMENT_EVIDENCE_TOOLS = {"overview", "search", "read_page", "crop", "ocr", "parse_table", "verify"}
NEGATIVE_EVIDENCE_TOOLS = {"search", "read_page"}


def _pct(numerator: int, denominator: int) -> float:
    return round(numerator / denominator, 4) if denominator else 0.0


def _load_json(path: Optional[str]) -> Optional[Dict[str, Any]]:
    if not path:
        return None
    path_obj = Path(path)
    if not path_obj.exists():
        return None
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _load_manual_labels(path: Optional[str]) -> Dict[str, Dict[str, Any]]:
    if not path:
        return {}
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    labels: Dict[str, Dict[str, Any]] = {}
    for line in path_obj.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        key = item.get("file") or item.get("rollout_file")
        if key:
            labels[str(key)] = item
    return labels


def _records_by_file(payload: Optional[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    if not payload:
        return {}
    records = payload.get("records", [])
    return {str(record["file"]): record for record in records if "file" in record}


def _observation_success(step: Dict[str, Any]) -> bool:
    return (step.get("observation") or {}).get("status") == "success"


def _successful_tools(payload: Dict[str, Any]) -> List[str]:
    return [
        str(step.get("action"))
        for step in payload.get("trajectory", [])
        if step.get("action") and _observation_success(step)
    ]


def _terminal_evidence_refs(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    for step in reversed(payload.get("trajectory", [])):
        if step.get("action") != payload.get("final_action"):
            continue
        action_input = step.get("action_input") or {}
        refs = action_input.get("evidence_refs")
        if isinstance(refs, list):
            return [ref for ref in refs if isinstance(ref, dict)]
    return []


def _claim_text(seed: Dict[str, Any], final_answer: str) -> str:
    if not seed.get("answerable", True):
        return "The requested information is not provided by the document."
    task_type = seed.get("task_type", "")
    if task_type == "verification":
        return f"The document supports the verification target: {final_answer}."
    return f"The answer to the question is: {final_answer}."


def _support_decision(
    payload: Dict[str, Any],
    answer_score: Dict[str, Any],
    path_record: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    seed = payload["seed"]
    final_action = payload.get("final_action")
    status = payload.get("status")
    final_answer = payload.get("final_answer") or ""
    answerable = bool(seed.get("answerable", True))
    successful_tools = _successful_tools(payload)
    document_evidence_tools = [tool for tool in successful_tools if tool in DOCUMENT_EVIDENCE_TOOLS]
    has_document_evidence = bool(document_evidence_tools)
    terminal_refs = _terminal_evidence_refs(payload)
    acceptable_path_ok = bool(path_record.get("acceptable_path_ok")) if path_record else None
    evidence_path_ok = bool(path_record.get("evidence_path_ok")) if path_record else has_document_evidence

    if status != "completed" or final_action not in TERMINAL_ACTIONS:
        support_label = "INVALID"
        sufficiency_label = "INVALID"
        failure_type = status or "invalid_terminal"
        filter_decision = "reject"
    elif not answerable:
        negative_tools_ok = NEGATIVE_EVIDENCE_TOOLS.issubset(set(successful_tools))
        if final_action != "refuse":
            support_label = "UNSUPPORTED"
            sufficiency_label = "INSUFFICIENT"
            failure_type = "should_refuse_but_answered"
            filter_decision = "reject"
        elif not negative_tools_ok:
            support_label = "INSUFFICIENT"
            sufficiency_label = "INSUFFICIENT"
            failure_type = "refusal_without_negative_evidence"
            filter_decision = "review"
        else:
            support_label = "SUPPORTED"
            sufficiency_label = "SUFFICIENT"
            failure_type = "none"
            filter_decision = "keep"
    elif not answer_score["answer_correct_adjusted"]:
        support_label = "UNSUPPORTED"
        sufficiency_label = "INSUFFICIENT" if has_document_evidence else "INSUFFICIENT"
        failure_type = answer_score["failure_category"]
        filter_decision = "reject"
    elif not has_document_evidence:
        support_label = "INSUFFICIENT"
        sufficiency_label = "INSUFFICIENT"
        failure_type = "answer_without_document_evidence"
        filter_decision = "review"
    elif acceptable_path_ok is False:
        support_label = "SUPPORTED"
        sufficiency_label = "SUFFICIENT"
        failure_type = "path_compliance_issue"
        filter_decision = "review"
    else:
        support_label = "SUPPORTED"
        sufficiency_label = "SUFFICIENT"
        failure_type = "none"
        filter_decision = "keep"

    return {
        "claim_text": _claim_text(seed, final_answer),
        "support_label": support_label,
        "sufficiency_label": sufficiency_label,
        "filter_decision": filter_decision,
        "failure_type": failure_type,
        "has_document_evidence": has_document_evidence,
        "successful_evidence_tools": document_evidence_tools,
        "terminal_evidence_refs": terminal_refs,
        "acceptable_path_ok": acceptable_path_ok,
        "evidence_path_ok": evidence_path_ok,
    }


def _manual_comparison(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    labeled = [record for record in records if record.get("human_support_label")]
    if not labeled:
        return {
            "manual_label_count": 0,
            "support_precision": None,
            "support_recall": None,
            "unsupported_identification_rate": None,
            "sufficiency_accuracy": None,
        }

    auto_supported = [record for record in labeled if record["support_label"] == "SUPPORTED"]
    human_supported = [record for record in labeled if record["human_support_label"] == "SUPPORTED"]
    supported_overlap = [
        record
        for record in labeled
        if record["support_label"] == "SUPPORTED" and record["human_support_label"] == "SUPPORTED"
    ]
    human_unsupported = [
        record
        for record in labeled
        if record["human_support_label"] in {"UNSUPPORTED", "INSUFFICIENT", "INVALID"}
    ]
    caught_unsupported = [
        record
        for record in human_unsupported
        if record["support_label"] in {"UNSUPPORTED", "INSUFFICIENT", "INVALID"}
    ]
    sufficiency_labeled = [record for record in labeled if record.get("human_sufficiency_label")]
    sufficiency_correct = [
        record
        for record in sufficiency_labeled
        if record["sufficiency_label"] == record["human_sufficiency_label"]
    ]

    return {
        "manual_label_count": len(labeled),
        "support_precision": _pct(len(supported_overlap), len(auto_supported)),
        "support_recall": _pct(len(supported_overlap), len(human_supported)),
        "unsupported_identification_rate": _pct(len(caught_unsupported), len(human_unsupported)),
        "sufficiency_accuracy": _pct(len(sufficiency_correct), len(sufficiency_labeled)),
    }


def _summarize(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    total = len(records)
    kept = [record for record in records if record["filter_decision"] == "keep"]
    return {
        "count": total,
        "auto_supported_rate": _pct(sum(record["support_label"] == "SUPPORTED" for record in records), total),
        "auto_sufficient_rate": _pct(sum(record["sufficiency_label"] == "SUFFICIENT" for record in records), total),
        "keep_rate": _pct(len(kept), total),
        "review_rate": _pct(sum(record["filter_decision"] == "review" for record in records), total),
        "reject_rate": _pct(sum(record["filter_decision"] == "reject" for record in records), total),
        "answer_adjusted_correct_rate": _pct(sum(record["answer_correct_adjusted"] for record in records), total),
        "document_evidence_rate": _pct(sum(record["has_document_evidence"] for record in records), total),
        "evidence_path_ok_rate": _pct(sum(bool(record["evidence_path_ok"]) for record in records), total),
        "acceptable_path_ok_rate": _pct(
            sum(record["acceptable_path_ok"] is True for record in records),
            sum(record["acceptable_path_ok"] is not None for record in records),
        ),
        "support_labels": dict(Counter(record["support_label"] for record in records)),
        "sufficiency_labels": dict(Counter(record["sufficiency_label"] for record in records)),
        "filter_decisions": dict(Counter(record["filter_decision"] for record in records)),
        "failure_types": dict(Counter(record["failure_type"] for record in records)),
    }


def evaluate(
    rollout_dir: Path,
    answer_eval_path: Optional[str],
    path_review_path: Optional[str],
    manual_labels_path: Optional[str],
) -> Dict[str, Any]:
    answer_eval = _load_json(answer_eval_path)
    path_review = _load_json(path_review_path)
    path_by_file = _records_by_file(path_review)
    manual_by_file = _load_manual_labels(manual_labels_path)

    records: List[Dict[str, Any]] = []
    for path in sorted(rollout_dir.glob("*/*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        display = display_path(str(path))
        answer_score = _score_rollout(payload)
        path_record = path_by_file.get(display) or path_by_file.get(str(path))
        support = _support_decision(payload, answer_score, path_record)
        manual = manual_by_file.get(display) or manual_by_file.get(str(path)) or {}
        record = {
            "file": display,
            "teacher": payload.get("teacher", {}).get("name"),
            "seed_id": payload["seed"].get("seed_id"),
            "task_type": payload["seed"].get("task_type"),
            "answerable": payload["seed"].get("answerable"),
            "question": payload["seed"].get("question"),
            "reference_answer": payload["seed"].get("reference_answer"),
            "final_action": payload.get("final_action"),
            "final_answer": payload.get("final_answer"),
            "status": payload.get("status"),
            "tool_sequence": payload.get("tool_sequence", []),
            "answer_correct_adjusted": answer_score["answer_correct_adjusted"],
            "answer_match_type": answer_score["answer_match_type"],
            "answer_failure_category": answer_score["failure_category"],
        }
        record.update(support)
        if manual:
            record["human_support_label"] = manual.get("human_support_label")
            record["human_sufficiency_label"] = manual.get("human_sufficiency_label")
            record["human_notes"] = manual.get("notes", "")
        records.append(record)

    by_teacher = defaultdict(list)
    by_task = defaultdict(list)
    for record in records:
        by_teacher[record["teacher"]].append(record)
        by_task[record["task_type"]].append(record)

    payload = {
        "rollout_dir": display_path(str(rollout_dir)),
        "answer_eval_path": display_path(answer_eval_path) if answer_eval_path else None,
        "path_review_path": display_path(path_review_path) if path_review_path else None,
        "manual_labels_path": display_path(manual_labels_path) if manual_labels_path else None,
        "overall": _summarize(records),
        "manual_comparison": _manual_comparison(records),
        "by_teacher": {key: _summarize(items) for key, items in sorted(by_teacher.items())},
        "by_task_type": {key: _summarize(items) for key, items in sorted(by_task.items())},
        "records": records,
    }
    return payload


def write_manual_template(path: Path, records: List[Dict[str, Any]]) -> None:
    lines = []
    for record in records:
        item = {
            "file": record["file"],
            "seed_id": record["seed_id"],
            "teacher": record["teacher"],
            "task_type": record["task_type"],
            "question": record["question"],
            "reference_answer": record["reference_answer"],
            "final_action": record["final_action"],
            "final_answer": record["final_answer"],
            "tool_sequence": record["tool_sequence"],
            "auto_support_label": record["support_label"],
            "auto_sufficiency_label": record["sufficiency_label"],
            "human_support_label": "",
            "human_sufficiency_label": "",
            "notes": "",
        }
        lines.append(json.dumps(item, ensure_ascii=False))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_markdown(path: Path, payload: Dict[str, Any]) -> None:
    overall = payload["overall"]
    manual = payload["manual_comparison"]
    lines = [
        "# Exp-3-lite Verification Review",
        "",
        f"- Rollout dir: `{payload['rollout_dir']}`",
        f"- Answer eval: `{payload['answer_eval_path']}`",
        f"- Path review: `{payload['path_review_path']}`",
        "",
        "## Overall",
        "",
        f"- Count: `{overall['count']}`",
        f"- Auto supported rate: `{overall['auto_supported_rate']:.2%}`",
        f"- Auto sufficient rate: `{overall['auto_sufficient_rate']:.2%}`",
        f"- Keep rate: `{overall['keep_rate']:.2%}`",
        f"- Review rate: `{overall['review_rate']:.2%}`",
        f"- Reject rate: `{overall['reject_rate']:.2%}`",
        f"- Adjusted answer correct rate: `{overall['answer_adjusted_correct_rate']:.2%}`",
        f"- Document evidence rate: `{overall['document_evidence_rate']:.2%}`",
        f"- Evidence path ok rate: `{overall['evidence_path_ok_rate']:.2%}`",
        f"- Acceptable path ok rate: `{overall['acceptable_path_ok_rate']:.2%}`",
        f"- Support labels: `{overall['support_labels']}`",
        f"- Sufficiency labels: `{overall['sufficiency_labels']}`",
        f"- Filter decisions: `{overall['filter_decisions']}`",
        f"- Failure types: `{overall['failure_types']}`",
        "",
        "## Manual Calibration",
        "",
        f"- Manual label count: `{manual['manual_label_count']}`",
        f"- Support precision: `{manual['support_precision']}`",
        f"- Support recall: `{manual['support_recall']}`",
        f"- Unsupported identification rate: `{manual['unsupported_identification_rate']}`",
        f"- Sufficiency accuracy: `{manual['sufficiency_accuracy']}`",
        "",
        "## By Task Type",
        "",
    ]
    for task_type, stats in payload["by_task_type"].items():
        lines.append(f"### {task_type}")
        lines.append(f"- Count: `{stats['count']}`")
        lines.append(f"- Auto supported rate: `{stats['auto_supported_rate']:.2%}`")
        lines.append(f"- Keep/review/reject: `{stats['filter_decisions']}`")
        lines.append(f"- Failure types: `{stats['failure_types']}`")
        lines.append("")

    lines.extend(["## Review / Reject Cases", ""])
    for record in payload["records"]:
        if record["filter_decision"] == "keep":
            continue
        lines.append(f"### {record['filter_decision']} | {record['failure_type']} | {record['teacher']} | {record['seed_id']}")
        lines.append(f"- File: `{record['file']}`")
        lines.append(f"- Task: `{record['task_type']}`")
        lines.append(f"- Tool sequence: `{record['tool_sequence']}`")
        lines.append(f"- Final: `{record['final_action']}` / `{record['final_answer']}`")
        lines.append(f"- Reference: `{record['reference_answer']}`")
        lines.append(f"- Support: `{record['support_label']}`, sufficiency: `{record['sufficiency_label']}`")
        lines.append("")

    lines.extend(
        [
            "## Label Schema",
            "",
            "- `SUPPORTED`: answer/refusal is supported by trajectory evidence.",
            "- `UNSUPPORTED`: final answer contradicts or fails to match the reference.",
            "- `INSUFFICIENT`: final decision may be plausible, but trajectory lacks enough document evidence.",
            "- `INVALID`: rollout did not terminate in a valid answer/refuse action.",
            "",
            "This is Exp-3-lite: it approximates DocVerify++ support/sufficiency using answer matching, evidence observations, path review, and optional human labels.",
            "A full Exp-3 should replace this heuristic support decision with claim decomposition plus DocVerify++ support judgment.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Exp-3-lite support/sufficiency verification over H2 rollouts.")
    parser.add_argument("--rollout-dir", default="data/h2/rollouts_v3", help="H2 rollout directory")
    parser.add_argument("--answer-eval", default="data/h2/eval_v3/summary.json", help="H2 answer evaluation JSON")
    parser.add_argument("--path-review", default="data/h2/eval_v3_path/path_review.json", help="H2 path review JSON")
    parser.add_argument("--manual-labels", default=None, help="Optional manual labels JSONL")
    parser.add_argument("--out-dir", default="data/h3/exp3_lite", help="Output directory")
    args = parser.parse_args()

    payload = evaluate(
        rollout_dir=Path(args.rollout_dir),
        answer_eval_path=args.answer_eval,
        path_review_path=args.path_review,
        manual_labels_path=args.manual_labels,
    )
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "support_review.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(out_dir / "support_review.md", payload)
    write_manual_template(out_dir / "manual_labels_template.jsonl", payload["records"])
    print(json.dumps(payload["overall"], ensure_ascii=False, indent=2))
    print(f"Exp-3-lite written to {out_dir}")


if __name__ == "__main__":
    main()
