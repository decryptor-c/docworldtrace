from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List

from ..utils import tokenize


def _display_path(path: str) -> str:
    path_obj = Path(path).expanduser()
    try:
        resolved = path_obj.resolve()
        cwd = Path.cwd().resolve()
        return str(resolved.relative_to(cwd))
    except (OSError, ValueError):
        return str(path_obj)


def _token_f1(reference: str, prediction: str) -> float:
    ref_tokens = tokenize(reference)
    pred_tokens = tokenize(prediction)
    if not ref_tokens and not pred_tokens:
        return 1.0
    if not ref_tokens or not pred_tokens:
        return 0.0
    ref_counts = defaultdict(int)
    pred_counts = defaultdict(int)
    for token in ref_tokens:
        ref_counts[token] += 1
    for token in pred_tokens:
        pred_counts[token] += 1
    overlap = 0
    for token in ref_counts:
        overlap += min(ref_counts[token], pred_counts.get(token, 0))
    if overlap == 0:
        return 0.0
    precision = overlap / len(pred_tokens)
    recall = overlap / len(ref_tokens)
    return 2 * precision * recall / (precision + recall)


def _compact_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def _numbers(value: str) -> List[float]:
    return [float(item) for item in re.findall(r"[-+]?\d+(?:\.\d+)?", value)]


def _has_percentage_point_unit(value: str) -> bool:
    normalized = value.lower()
    compact = _compact_text(value)
    return (
        "percentage point" in normalized
        or "percentage points" in normalized
        or "percentagepoint" in compact
        or "percentagepoints" in compact
    )


def _result_has_percentage_point_unit(reference: str, prediction: str) -> bool:
    ref_numbers = _numbers(reference)
    if not ref_numbers:
        return _has_percentage_point_unit(prediction)
    for ref_number in ref_numbers[:1]:
        pattern = re.compile(rf"(?<!\d){re.escape(str(ref_number).rstrip('0').rstrip('.'))}(?:\.0+)?(?!\d)")
        for match in pattern.finditer(prediction):
            window = prediction[match.start() : match.end() + 40].lower()
            if "percentage point" in window or "percentage points" in window:
                return True
    return False


def _numeric_match(reference: str, prediction: str) -> bool:
    ref_numbers = _numbers(reference)
    pred_numbers = _numbers(prediction)
    if not ref_numbers:
        return False
    return all(any(abs(ref - pred) <= 1e-6 for pred in pred_numbers) for ref in ref_numbers[:1])


def _contains_answer(reference: str, prediction: str, task_type: str) -> bool:
    ref_norm = _compact_text(reference)
    pred_norm = _compact_text(prediction)
    if not ref_norm or not pred_norm:
        return False
    if ref_norm in pred_norm:
        return True
    if task_type == "text_lookup" and ref_norm.startswith(pred_norm) and len(pred_norm) >= 8:
        return True
    return False


def _adjusted_answer_correct(seed: Dict[str, Any], final_action: str | None, final_answer: str) -> Dict[str, Any]:
    answerable = bool(seed.get("answerable", True))
    reference = seed["reference_answer"]
    task_type = seed["task_type"]
    if not answerable:
        return {
            "answer_correct_adjusted": final_action == "refuse",
            "answer_match_type": "refuse" if final_action == "refuse" else "not_refused",
            "numeric_match": False,
            "unit_correct": None,
        }
    if final_action != "answer":
        return {
            "answer_correct_adjusted": False,
            "answer_match_type": "no_answer",
            "numeric_match": False,
            "unit_correct": None,
        }
    if task_type == "numeric_computation":
        number_ok = _numeric_match(reference, final_answer)
        unit_ok = _result_has_percentage_point_unit(reference, final_answer) if _has_percentage_point_unit(reference) else True
        return {
            "answer_correct_adjusted": number_ok and unit_ok,
            "answer_match_type": "numeric_unit" if number_ok and unit_ok else "numeric_only" if number_ok else "numeric_mismatch",
            "numeric_match": number_ok,
            "unit_correct": unit_ok,
        }
    contains = _contains_answer(reference, final_answer, task_type)
    return {
        "answer_correct_adjusted": contains,
        "answer_match_type": "normalized_contains" if contains else "text_mismatch",
        "numeric_match": _numeric_match(reference, final_answer),
        "unit_correct": None,
    }


def _failure_category(score: Dict[str, Any]) -> str:
    if score["answer_correct_adjusted"]:
        if score["answer_correct"]:
            return "strict_correct"
        return "strict_eval_false_negative"
    if score["status"] == "format_error":
        return "format_error"
    if score["status"] == "budget_exhausted":
        return "budget_exhausted"
    if score["answer_match_type"] == "numeric_only":
        return "unit_error"
    if score["answer_correct"]:
        return "strict_metric_false_positive"
    if score["final_action"] == "refuse":
        return "incorrect_refusal"
    return "wrong_answer"


def _score_rollout(payload: Dict[str, Any]) -> Dict[str, Any]:
    seed = payload["seed"]
    final_action = payload.get("final_action")
    final_answer = payload.get("final_answer") or ""
    answerable = bool(seed.get("answerable", True))

    if answerable:
        answer_f1 = _token_f1(seed["reference_answer"], final_answer)
        answer_correct = answer_f1 >= 0.5 and final_action == "answer"
    else:
        answer_f1 = 1.0 if final_action == "refuse" else 0.0
        answer_correct = final_action == "refuse"

    adjusted = _adjusted_answer_correct(seed, final_action, final_answer)
    score = {
        "format_compliant": bool(payload["metrics"]["format_compliant"]),
        "terminated_normally": bool(payload["metrics"]["terminated_normally"]),
        "answer_correct": answer_correct,
        "answer_f1": answer_f1,
        "final_action": final_action,
        "final_answer": final_answer,
        "reference_answer": seed["reference_answer"],
        "step_count": int(payload["metrics"]["step_count"]),
        "used_verify": bool(payload["metrics"]["used_verify"]),
        "used_refuse": bool(payload["metrics"]["used_refuse"]),
        "direct_answer": bool(payload["metrics"]["direct_answer"]),
        "task_type": seed["task_type"],
        "seed_id": seed["seed_id"],
        "teacher": payload["teacher"]["name"],
        "status": payload["status"],
    }
    score.update(adjusted)
    score["failure_category"] = _failure_category(score)
    return score


def evaluate_rollout_dir(rollout_dir: str) -> Dict[str, Any]:
    root = Path(rollout_dir)
    files = sorted(root.glob("*/*.json"))
    if not files:
        raise SystemExit(f"No rollout JSON files found in {rollout_dir}")

    teacher_stats: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    records: List[Dict[str, Any]] = []
    for path in files:
        payload = json.loads(path.read_text())
        score = _score_rollout(payload)
        score["file"] = _display_path(str(path))
        teacher_stats[score["teacher"]].append(score)
        records.append(score)

    def summarize(items: List[Dict[str, Any]]) -> Dict[str, Any]:
        total = len(items)
        return {
            "count": total,
            "format_compliance_rate": round(sum(int(item["format_compliant"]) for item in items) / total, 4) if total else 0.0,
            "proper_termination_rate": round(sum(int(item["terminated_normally"]) for item in items) / total, 4) if total else 0.0,
            "answer_correct_rate": round(sum(int(item["answer_correct"]) for item in items) / total, 4) if total else 0.0,
            "answer_correct_adjusted_rate": round(sum(int(item["answer_correct_adjusted"]) for item in items) / total, 4) if total else 0.0,
            "mean_answer_f1": round(sum(item["answer_f1"] for item in items) / total, 4) if total else 0.0,
            "avg_steps": round(sum(item["step_count"] for item in items) / total, 4) if total else 0.0,
            "verify_usage_rate": round(sum(int(item["used_verify"]) for item in items) / total, 4) if total else 0.0,
            "refuse_usage_rate": round(sum(int(item["used_refuse"]) for item in items) / total, 4) if total else 0.0,
            "direct_answer_rate": round(sum(int(item["direct_answer"]) for item in items) / total, 4) if total else 0.0,
        }

    teacher_summary = {teacher: summarize(items) for teacher, items in teacher_stats.items()}
    overall = summarize(records)

    task_breakdown: Dict[str, Dict[str, Any]] = {}
    by_task: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for item in records:
        by_task[item["task_type"]].append(item)
    for task_type, items in by_task.items():
        task_breakdown[task_type] = summarize(items)

    payload = {
        "rollout_dir": _display_path(str(root)),
        "overall": overall,
        "by_teacher": teacher_summary,
        "by_task_type": task_breakdown,
        "records": records,
        "failure_categories": dict(sorted(defaultdict(int, ((category, sum(1 for item in records if item["failure_category"] == category)) for category in {item["failure_category"] for item in records})).items())),
    }
    return payload


def write_markdown(path: str, payload: Dict[str, Any]) -> None:
    lines = [
        "# Pilot Exp-2 Evaluation",
        "",
        f"- Rollout dir: `{payload['rollout_dir']}`",
        f"- Format compliance: `{payload['overall']['format_compliance_rate']:.2%}`",
        f"- Proper termination: `{payload['overall']['proper_termination_rate']:.2%}`",
        f"- Strict answer correct rate: `{payload['overall']['answer_correct_rate']:.2%}`",
        f"- Adjusted answer correct rate: `{payload['overall']['answer_correct_adjusted_rate']:.2%}`",
        f"- Mean answer F1: `{payload['overall']['mean_answer_f1']:.2%}`",
        f"- Avg steps: `{payload['overall']['avg_steps']}`",
        f"- Verify usage: `{payload['overall']['verify_usage_rate']:.2%}`",
        f"- Refuse usage: `{payload['overall']['refuse_usage_rate']:.2%}`",
        f"- Direct answer rate: `{payload['overall']['direct_answer_rate']:.2%}`",
        "",
        "## By Teacher",
        "",
    ]
    for teacher, summary in payload["by_teacher"].items():
        lines.append(f"### {teacher}")
        lines.append(f"- Count: `{summary['count']}`")
        lines.append(f"- Format compliance: `{summary['format_compliance_rate']:.2%}`")
        lines.append(f"- Proper termination: `{summary['proper_termination_rate']:.2%}`")
        lines.append(f"- Strict answer correct rate: `{summary['answer_correct_rate']:.2%}`")
        lines.append(f"- Adjusted answer correct rate: `{summary['answer_correct_adjusted_rate']:.2%}`")
        lines.append(f"- Mean answer F1: `{summary['mean_answer_f1']:.2%}`")
        lines.append(f"- Avg steps: `{summary['avg_steps']}`")
        lines.append("")

    lines.append("## By Task Type")
    lines.append("")
    for task_type, summary in payload["by_task_type"].items():
        lines.append(f"### {task_type}")
        lines.append(f"- Count: `{summary['count']}`")
        lines.append(f"- Strict answer correct rate: `{summary['answer_correct_rate']:.2%}`")
        lines.append(f"- Adjusted answer correct rate: `{summary['answer_correct_adjusted_rate']:.2%}`")
        lines.append(f"- Avg steps: `{summary['avg_steps']}`")
        lines.append("")

    lines.append("## Failure Categories")
    lines.append("")
    for category, count in payload.get("failure_categories", {}).items():
        lines.append(f"- {category}: `{count}`")
    lines.append("")

    Path(path).write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate H2 rollout logs.")
    parser.add_argument("--rollout-dir", default="data/h2/rollouts", help="Directory containing rollout JSONs")
    parser.add_argument("--out-json", default="data/h2/eval/summary.json", help="Output JSON summary")
    parser.add_argument("--out-md", default="data/h2/eval/summary.md", help="Output Markdown summary")
    args = parser.parse_args()

    payload = evaluate_rollout_dir(args.rollout_dir)
    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(args.out_md, payload)
    print(json.dumps(payload["overall"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
