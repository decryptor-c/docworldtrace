from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional

from ..docverify import DocVerifyPlus
from .h2_eval import _score_rollout
from .h2_rollout import display_path


def _pct(numerator: int, denominator: int) -> float:
    return round(numerator / denominator, 4) if denominator else 0.0


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


def _summarize(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    total = len(records)
    return {
        "count": total,
        "support_rate": _pct(sum(record["docverify"]["support_label"] == "SUPPORTED" for record in records), total),
        "sufficiency_rate": _pct(sum(record["docverify"]["sufficiency"] == "SUFFICIENT" for record in records), total),
        "keep_rate": _pct(sum(record["docverify"]["filter_decision"] == "keep" for record in records), total),
        "review_rate": _pct(sum(record["docverify"]["filter_decision"] == "review" for record in records), total),
        "reject_rate": _pct(sum(record["docverify"]["filter_decision"] == "reject" for record in records), total),
        "adjusted_answer_correct_rate": _pct(sum(record["answer_correct_adjusted"] for record in records), total),
        "mean_quality_score": round(
            sum(record["docverify"]["reward_signals"]["quality_score"] for record in records) / total,
            4,
        )
        if total
        else 0.0,
        "support_labels": dict(Counter(record["docverify"]["support_label"] for record in records)),
        "sufficiency_labels": dict(Counter(record["docverify"]["sufficiency"] for record in records)),
        "filter_decisions": dict(Counter(record["docverify"]["filter_decision"] for record in records)),
        "failure_taxonomy": dict(Counter(record["docverify"].get("failure_taxonomy") or "none" for record in records)),
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
    auto_supported = [record for record in labeled if record["docverify"]["support_label"] == "SUPPORTED"]
    human_supported = [record for record in labeled if record["human_support_label"] == "SUPPORTED"]
    true_supported = [
        record
        for record in labeled
        if record["docverify"]["support_label"] == "SUPPORTED" and record["human_support_label"] == "SUPPORTED"
    ]
    human_bad = [
        record
        for record in labeled
        if record["human_support_label"] in {"PARTIAL", "NOT_SUPPORTED", "INSUFFICIENT", "INVALID"}
    ]
    caught_bad = [
        record
        for record in human_bad
        if record["docverify"]["support_label"] in {"PARTIAL", "NOT_SUPPORTED"}
        or record["docverify"]["sufficiency"] in {"INSUFFICIENT", "MISSING"}
    ]
    suff_labeled = [record for record in labeled if record.get("human_sufficiency")]
    suff_correct = [
        record
        for record in suff_labeled
        if record["docverify"]["sufficiency"] == record["human_sufficiency"]
    ]
    return {
        "manual_label_count": len(labeled),
        "support_precision": _pct(len(true_supported), len(auto_supported)),
        "support_recall": _pct(len(true_supported), len(human_supported)),
        "unsupported_identification_rate": _pct(len(caught_bad), len(human_bad)),
        "sufficiency_accuracy": _pct(len(suff_correct), len(suff_labeled)),
    }


def evaluate(rollout_dir: Path, manual_labels: Optional[str], top_k: int) -> Dict[str, Any]:
    verifier = DocVerifyPlus(top_k=top_k)
    labels = _load_manual_labels(manual_labels)
    records: List[Dict[str, Any]] = []
    for path in sorted(rollout_dir.glob("*/*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        display = display_path(str(path))
        answer_score = _score_rollout(payload)
        docverify = verifier.verify_rollout(payload)
        manual = labels.get(display) or labels.get(str(path)) or {}
        record = {
            "file": display,
            "teacher": payload.get("teacher", {}).get("name"),
            "seed_id": payload["seed"].get("seed_id"),
            "task_type": payload["seed"].get("task_type"),
            "question": payload["seed"].get("question"),
            "reference_answer": payload["seed"].get("reference_answer"),
            "answerable": payload["seed"].get("answerable"),
            "status": payload.get("status"),
            "tool_sequence": payload.get("tool_sequence", []),
            "final_action": payload.get("final_action"),
            "final_answer": payload.get("final_answer"),
            "answer_correct_adjusted": answer_score["answer_correct_adjusted"],
            "answer_match_type": answer_score["answer_match_type"],
            "answer_failure_category": answer_score["failure_category"],
            "docverify": docverify,
        }
        if manual:
            record["human_support_label"] = manual.get("human_support_label")
            record["human_sufficiency"] = manual.get("human_sufficiency")
            record["human_notes"] = manual.get("notes", "")
        records.append(record)

    by_teacher = defaultdict(list)
    by_task = defaultdict(list)
    for record in records:
        by_teacher[record["teacher"]].append(record)
        by_task[record["task_type"]].append(record)
    return {
        "rollout_dir": display_path(str(rollout_dir)),
        "manual_labels": display_path(manual_labels) if manual_labels else None,
        "verifier": "DocVerifyPlus(rule_claim_evidence_v1)",
        "overall": _summarize(records),
        "manual_comparison": _manual_comparison(records),
        "by_teacher": {key: _summarize(items) for key, items in sorted(by_teacher.items())},
        "by_task_type": {key: _summarize(items) for key, items in sorted(by_task.items())},
        "records": records,
    }


def write_markdown(path: Path, payload: Dict[str, Any]) -> None:
    overall = payload["overall"]
    lines = [
        "# Exp-3 DocVerify++ Review",
        "",
        f"- Rollout dir: `{payload['rollout_dir']}`",
        f"- Verifier: `{payload['verifier']}`",
        "",
        "## Overall",
        "",
        f"- Count: `{overall['count']}`",
        f"- Support rate: `{overall['support_rate']:.2%}`",
        f"- Sufficiency rate: `{overall['sufficiency_rate']:.2%}`",
        f"- Keep rate: `{overall['keep_rate']:.2%}`",
        f"- Review rate: `{overall['review_rate']:.2%}`",
        f"- Reject rate: `{overall['reject_rate']:.2%}`",
        f"- Adjusted answer correct rate: `{overall['adjusted_answer_correct_rate']:.2%}`",
        f"- Mean quality score: `{overall['mean_quality_score']}`",
        f"- Support labels: `{overall['support_labels']}`",
        f"- Sufficiency labels: `{overall['sufficiency_labels']}`",
        f"- Filter decisions: `{overall['filter_decisions']}`",
        f"- Failure taxonomy: `{overall['failure_taxonomy']}`",
        "",
        "## Manual Calibration",
        "",
    ]
    for key, value in payload["manual_comparison"].items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## By Task Type", ""])
    for task_type, stats in payload["by_task_type"].items():
        lines.append(f"### {task_type}")
        lines.append(f"- Count: `{stats['count']}`")
        lines.append(f"- Support rate: `{stats['support_rate']:.2%}`")
        lines.append(f"- Sufficiency rate: `{stats['sufficiency_rate']:.2%}`")
        lines.append(f"- Keep/review/reject: `{stats['filter_decisions']}`")
        lines.append(f"- Failure taxonomy: `{stats['failure_taxonomy']}`")
        lines.append("")

    lines.extend(["## Review / Reject Cases", ""])
    for record in payload["records"]:
        decision = record["docverify"]["filter_decision"]
        if decision == "keep":
            continue
        lines.append(f"### {decision} | {record['docverify'].get('failure_taxonomy')} | {record['teacher']} | {record['seed_id']}")
        lines.append(f"- File: `{record['file']}`")
        lines.append(f"- Task: `{record['task_type']}`")
        lines.append(f"- Tool sequence: `{record['tool_sequence']}`")
        lines.append(f"- Final: `{record['final_action']}` / `{record['final_answer']}`")
        lines.append(f"- Reference: `{record['reference_answer']}`")
        lines.append(f"- Support: `{record['docverify']['support_label']}`")
        lines.append(f"- Sufficiency: `{record['docverify']['sufficiency']}`")
        lines.append(f"- Quality score: `{record['docverify']['reward_signals']['quality_score']}`")
        for judgment in record["docverify"]["claim_judgments"]:
            lines.append(f"- Claim `{judgment['claim_id']}`: `{judgment['label']}` / `{judgment['rationale']}`")
        lines.append("")
    lines.extend(
        [
            "## Notes",
            "",
            "This implementation performs the full DocVerify++ pipeline for the pilot setting: claim decomposition, evidence collection from trajectory observations, evidence ranking, claim-evidence support judgment, sufficiency judgment, reward scoring, filtering, and optional human calibration.",
            "The current support judge is a deterministic rule/NLI-lite implementation. It is suitable for pilot filtering and auditing; it can be replaced by an external NLI or LLM judge without changing the output schema.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


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
            "final_answer": record["final_answer"],
            "tool_sequence": record["tool_sequence"],
            "auto_support_label": record["docverify"]["support_label"],
            "auto_sufficiency": record["docverify"]["sufficiency"],
            "auto_filter_decision": record["docverify"]["filter_decision"],
            "human_support_label": "",
            "human_sufficiency": "",
            "notes": "",
        }
        lines.append(json.dumps(item, ensure_ascii=False))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run full DocVerify++ review over H2 rollouts.")
    parser.add_argument("--rollout-dir", default="data/h2/rollouts_v3")
    parser.add_argument("--out-dir", default="data/h3/docverify_plus")
    parser.add_argument("--manual-labels", default=None)
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()

    payload = evaluate(Path(args.rollout_dir), args.manual_labels, args.top_k)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "docverify_review.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(out_dir / "docverify_review.md", payload)
    write_manual_template(out_dir / "manual_labels_template.jsonl", payload["records"])
    print(json.dumps(payload["overall"], ensure_ascii=False, indent=2))
    print(f"DocVerify++ review written to {out_dir}")


if __name__ == "__main__":
    main()
