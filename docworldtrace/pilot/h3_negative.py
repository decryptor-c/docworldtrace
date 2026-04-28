from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

from .h2_rollout import display_path
from .h3_docverify import evaluate as evaluate_docverify
from .h3_docverify import write_markdown as write_docverify_markdown
from .h3_docverify import write_manual_template

EXTENDED_CORRUPTION_TYPES = {
    "hallucinated_evidence_ref",
    "compute_expression_mismatch",
    "verify_label_mismatch",
}

NATURAL_LIKE_CORRUPTION_TYPES = {
    "over_refusal_for_answerable",
    "direct_answer_without_tools",
    "numeric_near_miss",
    "dropped_compute_step",
    "table_row_label_as_answer",
    "weak_search_only_evidence",
}

NUMBER_RE = re.compile(r"[-+]?\d+(?:\.\d+)?")


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _is_terminal_action(action: Any) -> bool:
    return action in {"answer", "refuse"}


def _last_terminal_step(payload: Dict[str, Any]) -> Dict[str, Any] | None:
    for step in reversed(payload.get("trajectory", [])):
        if _is_terminal_action(step.get("action")):
            return step
    return None


def _set_terminal(payload: Dict[str, Any], action: str, text: str) -> None:
    payload["final_action"] = action
    payload["final_answer"] = text
    terminal = _last_terminal_step(payload)
    if terminal is None:
        terminal = {
            "step": len(payload.get("trajectory", [])) + 1,
            "raw_model_output": "",
            "format_valid": True,
            "execution_valid": True,
        }
        payload.setdefault("trajectory", []).append(terminal)
    terminal["action"] = action
    terminal["thought"] = "Corrupted negative-control terminal action."
    if action == "answer":
        terminal["action_input"] = {"text": text, "evidence_refs": payload.get("seed", {}).get("supporting_refs", [])}
    else:
        terminal["action_input"] = {"reason": text}
    terminal["observation"] = {
        "action": action,
        "status": "success",
        "result": terminal["action_input"],
        "provenance": {"page": None, "bbox": None, "element_type": "negative_control"},
        "confidence": 0.0,
        "cache_hit": False,
    }
    terminal["raw_model_output"] = json.dumps(
        {
            "thought": terminal["thought"],
            "action": action,
            "action_input": terminal["action_input"],
        },
        ensure_ascii=False,
    )
    payload["tool_sequence"] = [step.get("action") for step in payload.get("trajectory", []) if step.get("action")]
    metrics = dict(payload.get("metrics", {}))
    metrics["terminated_normally"] = True
    metrics["format_compliant"] = True
    metrics["used_refuse"] = action == "refuse"
    metrics["used_verify"] = "verify" in payload["tool_sequence"]
    nonterminal = [item for item in payload["tool_sequence"] if item not in {"answer", "refuse"}]
    metrics["direct_answer"] = bool(action in {"answer", "refuse"} and not nonterminal)
    metrics["step_count"] = len(payload.get("trajectory", []))
    payload["metrics"] = metrics


def _remove_evidence_observations(payload: Dict[str, Any]) -> None:
    for step in payload.get("trajectory", []):
        if step.get("action") in {"answer", "refuse"}:
            continue
        step["observation"] = {
            "action": step.get("action"),
            "status": "success",
            "result": {},
            "provenance": {"page": None, "bbox": None, "element_type": "corrupted_empty_evidence"},
            "confidence": 0.0,
            "cache_hit": False,
        }


def _set_terminal_evidence_refs(payload: Dict[str, Any], evidence_refs: List[Dict[str, Any]]) -> None:
    terminal = _last_terminal_step(payload)
    if terminal is None:
        return
    terminal.setdefault("action_input", {})["evidence_refs"] = evidence_refs
    result = (terminal.setdefault("observation", {}).setdefault("result", {}))
    if isinstance(result, dict):
        result["evidence_refs"] = evidence_refs


def _flip_label(label: str | None) -> str:
    return "UNSUPPORTED" if str(label or "").upper() == "SUPPORTED" else "SUPPORTED"


def _numbers(value: str) -> List[float]:
    return [float(item) for item in NUMBER_RE.findall(value or "")]


def _refresh_sequence_and_metrics(payload: Dict[str, Any]) -> None:
    payload["tool_sequence"] = [step.get("action") for step in payload.get("trajectory", []) if step.get("action")]
    metrics = dict(payload.get("metrics", {}))
    sequence = payload["tool_sequence"]
    metrics["used_refuse"] = "refuse" in sequence
    metrics["used_verify"] = "verify" in sequence
    nonterminal = [item for item in sequence if item not in {"answer", "refuse"}]
    metrics["direct_answer"] = bool(sequence and sequence[-1] in {"answer", "refuse"} and not nonterminal)
    metrics["step_count"] = len(payload.get("trajectory", []))
    metrics["terminated_normally"] = bool(sequence and sequence[-1] in {"answer", "refuse"})
    metrics["format_compliant"] = True
    payload["metrics"] = metrics


def _set_corruption_metadata(
    corrupted: Dict[str, Any],
    source: Dict[str, Any],
    corruption_type: str,
    rationale: str,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    corrupted["condition"] = "h3_negative_control"
    corrupted["corruption"] = {
        "type": corruption_type,
        "source_teacher": source.get("teacher", {}).get("name"),
        "source_seed_id": source.get("seed", {}).get("seed_id"),
        "source_final_action": source.get("final_action"),
        "source_final_answer": source.get("final_answer"),
        "expected_human_label": "BAD_TRAJECTORY",
        "expected_filter_decision": "reject_or_review",
        "rationale": rationale,
    }
    corrupted["teacher"] = {
        **dict(corrupted.get("teacher", {})),
        "name": f"{corrupted.get('teacher', {}).get('name', 'teacher')}__negative",
    }
    return corrupted, corrupted["corruption"]


def _wrong_answer_for(payload: Dict[str, Any]) -> Tuple[str, str]:
    seed = payload["seed"]
    task_type = seed.get("task_type")
    if not seed.get("answerable", True):
        return "answer", "The private mobile phone number is 555-0100."
    if task_type == "verification":
        reference = str(seed.get("reference_answer", "")).upper()
        flipped = "UNSUPPORTED" if reference == "SUPPORTED" else "SUPPORTED"
        return "answer", flipped
    if task_type == "numeric_computation":
        return "answer", "999 percentage points"
    if task_type == "table_lookup":
        return "answer", "NOT_IN_TABLE"
    return "answer", "Incorrect heading not supported by the document"


def corrupt_payload(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    corrupted = deepcopy(payload)
    seed = corrupted["seed"]
    action, text = _wrong_answer_for(corrupted)
    _set_terminal(corrupted, action, text)
    corruption_type = "false_answer_for_unanswerable" if not seed.get("answerable", True) else "wrong_final_answer"
    corrupted["condition"] = "h3_negative_control"
    corrupted["corruption"] = {
        "type": corruption_type,
        "source_teacher": payload.get("teacher", {}).get("name"),
        "source_seed_id": seed.get("seed_id"),
        "source_final_action": payload.get("final_action"),
        "source_final_answer": payload.get("final_answer"),
        "expected_human_label": "BAD_TRAJECTORY",
        "expected_filter_decision": "reject_or_review",
        "rationale": "The terminal answer/refusal was intentionally corrupted while preserving the preceding trajectory.",
    }
    corrupted["teacher"] = {
        **dict(corrupted.get("teacher", {})),
        "name": f"{corrupted.get('teacher', {}).get('name', 'teacher')}__negative",
    }
    return corrupted, corrupted["corruption"]


def corrupt_payload_over_refusal(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]] | None:
    if not payload.get("seed", {}).get("answerable", True):
        return None
    corrupted = deepcopy(payload)
    _set_terminal(
        corrupted,
        "refuse",
        "I cannot answer because the document does not provide sufficient evidence.",
    )
    return _set_corruption_metadata(
        corrupted,
        payload,
        "over_refusal_for_answerable",
        "The trajectory previously answered an answerable question, but the terminal action is changed to refusal.",
    )


def corrupt_payload_direct_answer_without_tools(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]] | None:
    if payload.get("final_action") != "answer":
        return None
    corrupted = deepcopy(payload)
    terminal = deepcopy(_last_terminal_step(corrupted))
    if terminal is None:
        return None
    terminal["step"] = 1
    terminal["thought"] = "Answering directly without using document tools."
    terminal["raw_model_output"] = json.dumps(
        {
            "thought": terminal["thought"],
            "action": "answer",
            "action_input": terminal.get("action_input", {}),
        },
        ensure_ascii=False,
    )
    corrupted["trajectory"] = [terminal]
    _refresh_sequence_and_metrics(corrupted)
    return _set_corruption_metadata(
        corrupted,
        payload,
        "direct_answer_without_tools",
        "The final answer text is preserved, but all supporting tool calls and observations are removed.",
    )


def corrupt_payload_numeric_near_miss(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]] | None:
    seed = payload.get("seed", {})
    if seed.get("task_type") != "numeric_computation" or payload.get("final_action") != "answer":
        return None
    reference_numbers = _numbers(str(seed.get("reference_answer", "")))
    if not reference_numbers:
        return None
    wrong_value = reference_numbers[0] + 1.0
    unit = " percentage points" if "percentage point" in str(seed.get("reference_answer", "")).lower() else ""
    corrupted = deepcopy(payload)
    _set_terminal(corrupted, "answer", f"{wrong_value:g}{unit}")
    return _set_corruption_metadata(
        corrupted,
        payload,
        "numeric_near_miss",
        "The terminal numeric answer is changed to a plausible but incorrect nearby value.",
    )


def corrupt_payload_dropped_compute(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]] | None:
    seed = payload.get("seed", {})
    if seed.get("task_type") != "numeric_computation" or payload.get("final_action") != "answer":
        return None
    if "compute" not in payload.get("tool_sequence", []):
        return None
    corrupted = deepcopy(payload)
    corrupted["trajectory"] = [step for step in corrupted.get("trajectory", []) if step.get("action") != "compute"]
    for index, step in enumerate(corrupted["trajectory"], start=1):
        step["step"] = index
    _refresh_sequence_and_metrics(corrupted)
    return _set_corruption_metadata(
        corrupted,
        payload,
        "dropped_compute_step",
        "The final numeric answer is preserved, but the compute provenance step is removed.",
    )


def corrupt_payload_table_row_label(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]] | None:
    seed = payload.get("seed", {})
    if seed.get("task_type") != "table_lookup" or payload.get("final_action") != "answer":
        return None
    corrupted = deepcopy(payload)
    question = str(seed.get("question", ""))
    row_label = question.split("'")[1] if "'" in question and len(question.split("'")) > 2 else "the requested row label"
    _set_terminal(corrupted, "answer", row_label)
    return _set_corruption_metadata(
        corrupted,
        payload,
        "table_row_label_as_answer",
        "The answer is replaced with a plausible table row label rather than the requested cell value.",
    )


def corrupt_payload_weak_search_only_evidence(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]] | None:
    if payload.get("final_action") != "answer" or not payload.get("seed", {}).get("answerable", True):
        return None
    if "search" not in payload.get("tool_sequence", []):
        return None
    corrupted = deepcopy(payload)
    for step in corrupted.get("trajectory", []):
        if step.get("action") in {"search", "answer", "refuse"}:
            continue
        step["observation"] = {
            "action": step.get("action"),
            "status": "success",
            "result": {},
            "provenance": {"page": None, "bbox": None, "element_type": "corrupted_weak_evidence"},
            "confidence": 0.0,
            "cache_hit": False,
        }
    return _set_corruption_metadata(
        corrupted,
        payload,
        "weak_search_only_evidence",
        "The final answer is preserved, but rich evidence observations are blanked so only search-level evidence remains.",
    )


def corrupt_payload_missing_evidence(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    corrupted = deepcopy(payload)
    _remove_evidence_observations(corrupted)
    corrupted["condition"] = "h3_negative_control"
    corrupted["corruption"] = {
        "type": "missing_evidence_observations",
        "source_teacher": payload.get("teacher", {}).get("name"),
        "source_seed_id": payload.get("seed", {}).get("seed_id"),
        "source_final_action": payload.get("final_action"),
        "source_final_answer": payload.get("final_answer"),
        "expected_human_label": "BAD_TRAJECTORY",
        "expected_filter_decision": "reject_or_review",
        "rationale": "The final answer is preserved but all non-terminal evidence observations were blanked.",
    }
    corrupted["teacher"] = {
        **dict(corrupted.get("teacher", {})),
        "name": f"{corrupted.get('teacher', {}).get('name', 'teacher')}__negative",
    }
    return corrupted, corrupted["corruption"]


def corrupt_payload_hallucinated_evidence_ref(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]] | None:
    if payload.get("final_action") != "answer":
        return None
    corrupted = deepcopy(payload)
    _set_terminal_evidence_refs(corrupted, [{"page": 999999, "bbox": [0, 0, 1, 1]}])
    corrupted["condition"] = "h3_negative_control"
    corrupted["corruption"] = {
        "type": "hallucinated_evidence_ref",
        "source_teacher": payload.get("teacher", {}).get("name"),
        "source_seed_id": payload.get("seed", {}).get("seed_id"),
        "source_final_action": payload.get("final_action"),
        "source_final_answer": payload.get("final_answer"),
        "expected_human_label": "BAD_TRAJECTORY",
        "expected_filter_decision": "reject_or_review",
        "rationale": "The final answer is preserved, but terminal evidence_refs point to a page never observed in the trajectory.",
    }
    corrupted["teacher"] = {
        **dict(corrupted.get("teacher", {})),
        "name": f"{corrupted.get('teacher', {}).get('name', 'teacher')}__negative",
    }
    return corrupted, corrupted["corruption"]


def corrupt_payload_compute_expression_mismatch(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]] | None:
    if payload.get("seed", {}).get("task_type") != "numeric_computation" or payload.get("final_action") != "answer":
        return None
    corrupted = deepcopy(payload)
    changed = False
    for step in corrupted.get("trajectory", []):
        if step.get("action") != "compute":
            continue
        observation = step.get("observation") or {}
        if observation.get("status") != "success":
            continue
        result = observation.setdefault("result", {})
        if "value" not in result:
            continue
        result["expr"] = "bad_left + bad_right"
        result["vars"] = {"bad_left": 123.0, "bad_right": 456.0}
        step.setdefault("action_input", {})["expr"] = "bad_left + bad_right"
        step.setdefault("action_input", {})["vars"] = {"bad_left": 123.0, "bad_right": 456.0}
        changed = True
        break
    if not changed:
        return None
    corrupted["condition"] = "h3_negative_control"
    corrupted["corruption"] = {
        "type": "compute_expression_mismatch",
        "source_teacher": payload.get("teacher", {}).get("name"),
        "source_seed_id": payload.get("seed", {}).get("seed_id"),
        "source_final_action": payload.get("final_action"),
        "source_final_answer": payload.get("final_answer"),
        "expected_human_label": "BAD_TRAJECTORY",
        "expected_filter_decision": "reject_or_review",
        "rationale": "The final answer is preserved, but a successful compute step now has an expression/vars provenance that recomputes to a different value.",
    }
    corrupted["teacher"] = {
        **dict(corrupted.get("teacher", {})),
        "name": f"{corrupted.get('teacher', {}).get('name', 'teacher')}__negative",
    }
    return corrupted, corrupted["corruption"]


def corrupt_payload_verify_label_mismatch(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]] | None:
    if payload.get("seed", {}).get("task_type") != "verification" or payload.get("final_action") != "answer":
        return None
    corrupted = deepcopy(payload)
    changed = False
    for step in corrupted.get("trajectory", []):
        if step.get("action") != "verify":
            continue
        result = (step.get("observation") or {}).get("result") or {}
        if "label" not in result:
            continue
        result["label"] = _flip_label(result.get("label"))
        result["sufficiency"] = "INSUFFICIENT"
        changed = True
        break
    if not changed:
        return None
    corrupted["condition"] = "h3_negative_control"
    corrupted["corruption"] = {
        "type": "verify_label_mismatch",
        "source_teacher": payload.get("teacher", {}).get("name"),
        "source_seed_id": payload.get("seed", {}).get("seed_id"),
        "source_final_action": payload.get("final_action"),
        "source_final_answer": payload.get("final_answer"),
        "expected_human_label": "BAD_TRAJECTORY",
        "expected_filter_decision": "reject_or_review",
        "rationale": "The final answer is preserved, but the verify observation label is flipped to disagree with the expected verification label.",
    }
    corrupted["teacher"] = {
        **dict(corrupted.get("teacher", {})),
        "name": f"{corrupted.get('teacher', {}).get('name', 'teacher')}__negative",
    }
    return corrupted, corrupted["corruption"]


def build_negative_rollouts(
    source_rollout_dir: Path,
    out_rollout_dir: Path,
    include_missing_evidence: bool,
    include_extended_corruptions: bool,
    include_natural_like_corruptions: bool,
    max_per_type: int | None,
) -> Dict[str, Any]:
    out_rollout_dir.mkdir(parents=True, exist_ok=True)
    source_files = sorted(source_rollout_dir.glob("*/*.json"))
    type_counts: Counter[str] = Counter()
    manifest = []
    for source_path in source_files:
        payload = _load_json(source_path)
        if payload.get("status") != "completed" or payload.get("final_action") not in {"answer", "refuse"}:
            continue
        corrupted_items: List[Tuple[Dict[str, Any], Dict[str, Any]]] = [corrupt_payload(payload)]
        if include_missing_evidence and payload.get("seed", {}).get("answerable", True):
            corrupted_items.append(corrupt_payload_missing_evidence(payload))
        if include_extended_corruptions:
            for builder in [
                corrupt_payload_hallucinated_evidence_ref,
                corrupt_payload_compute_expression_mismatch,
                corrupt_payload_verify_label_mismatch,
            ]:
                item = builder(payload)
                if item is not None:
                    corrupted_items.append(item)
        if include_natural_like_corruptions:
            for builder in [
                corrupt_payload_over_refusal,
                corrupt_payload_direct_answer_without_tools,
                corrupt_payload_numeric_near_miss,
                corrupt_payload_dropped_compute,
                corrupt_payload_table_row_label,
                corrupt_payload_weak_search_only_evidence,
            ]:
                item = builder(payload)
                if item is not None:
                    corrupted_items.append(item)
        for corrupted, corruption in corrupted_items:
            corruption_type = corruption["type"]
            if max_per_type is not None and type_counts[corruption_type] >= max_per_type:
                continue
            type_counts[corruption_type] += 1
            teacher = corrupted["teacher"]["name"]
            stem = source_path.stem
            out_path = out_rollout_dir / teacher / f"{stem}__{corruption_type}.json"
            _write_json(out_path, corrupted)
            manifest.append(
                {
                    "source_file": display_path(str(source_path)),
                    "negative_file": display_path(str(out_path)),
                    "seed_id": payload["seed"].get("seed_id"),
                    "task_type": payload["seed"].get("task_type"),
                    "corruption_type": corruption_type,
                    "source_final_action": corruption["source_final_action"],
                    "source_final_answer": corruption["source_final_answer"],
                    "corrupted_final_action": corrupted.get("final_action"),
                    "corrupted_final_answer": corrupted.get("final_answer"),
                    "expected_filter_decision": corruption["expected_filter_decision"],
                }
            )
    summary = {
        "source_rollout_dir": display_path(str(source_rollout_dir)),
        "negative_rollout_dir": display_path(str(out_rollout_dir)),
        "negative_count": len(manifest),
        "corruption_counts": dict(type_counts),
        "manifest": manifest,
    }
    _write_json(out_rollout_dir / "negative_manifest.json", summary)
    return summary


def _load_manifest(path: Path) -> Dict[str, Dict[str, Any]]:
    manifest_path = path / "negative_manifest.json"
    if not manifest_path.exists():
        return {}
    payload = _load_json(manifest_path)
    return {item["negative_file"]: item for item in payload.get("manifest", [])}


def evaluate_negative(negative_rollout_dir: Path, out_dir: Path, top_k: int) -> Dict[str, Any]:
    review = evaluate_docverify(negative_rollout_dir, manual_labels=None, top_k=top_k)
    manifest = _load_manifest(negative_rollout_dir)
    records = []
    caught = 0
    missed_keep = 0
    for record in review["records"]:
        item = dict(record)
        decision = item["docverify"]["filter_decision"]
        item["negative_expected"] = manifest.get(item["file"], {})
        item["negative_caught"] = decision in {"reject", "review"}
        caught += int(item["negative_caught"])
        missed_keep += int(decision == "keep")
        records.append(item)
    review["records"] = records
    review["negative_eval"] = {
        "negative_count": len(records),
        "caught_bad_rate": round(caught / len(records), 4) if records else 0.0,
        "missed_keep_rate": round(missed_keep / len(records), 4) if records else 0.0,
        "caught_bad_count": caught,
        "missed_keep_count": missed_keep,
        "filter_decisions": dict(Counter(record["docverify"]["filter_decision"] for record in records)),
        "support_labels": dict(Counter(record["docverify"]["support_label"] for record in records)),
        "failure_taxonomy": dict(Counter(record["docverify"].get("failure_taxonomy") or "none" for record in records)),
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_json(out_dir / "negative_docverify_review.json", review)
    write_docverify_markdown(out_dir / "negative_docverify_review.md", review)
    write_negative_manual_review(out_dir / "negative_manual_review.md", records)
    write_negative_manual_jsonl(out_dir / "negative_manual_review.jsonl", records)
    write_manual_template(out_dir / "negative_manual_labels_template.jsonl", records)
    return review


def write_negative_manual_jsonl(path: Path, records: List[Dict[str, Any]]) -> None:
    rows = []
    for record in records:
        expected = record.get("negative_expected", {})
        rows.append(
            {
                "file": record["file"],
                "source_file": expected.get("source_file"),
                "seed_id": record["seed_id"],
                "task_type": record["task_type"],
                "corruption_type": expected.get("corruption_type"),
                "question": record["question"],
                "reference_answer": record["reference_answer"],
                "source_final_answer": expected.get("source_final_answer"),
                "corrupted_final_answer": record["final_answer"],
                "tool_sequence": record["tool_sequence"],
                "auto_support_label": record["docverify"]["support_label"],
                "auto_sufficiency": record["docverify"]["sufficiency"],
                "auto_filter_decision": record["docverify"]["filter_decision"],
                "auto_failure_taxonomy": record["docverify"].get("failure_taxonomy"),
                "negative_caught": record["negative_caught"],
                "human_bad_trajectory": "",
                "human_expected_decision": "",
                "notes": "",
            }
        )
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")


def write_negative_manual_review(path: Path, records: List[Dict[str, Any]]) -> None:
    lines = [
        "# H3 Negative-Control Manual Review",
        "",
        "目的：人工审查 DocVerify++ 对 corrupted / bad trajectories 的识别是否合理。",
        "",
        "| # | Caught? | Decision | Failure | Corruption | Seed | Task | Reference | Corrupted Final | Human Notes |",
        "|---:|---:|---|---|---|---|---|---|---|---|",
    ]
    for index, record in enumerate(records, start=1):
        expected = record.get("negative_expected", {})
        lines.append(
            "| {idx} | {caught} | `{decision}` | `{failure}` | `{corr}` | `{seed}` | `{task}` | `{ref}` | `{final}` |  |".format(
                idx=index,
                caught="YES" if record["negative_caught"] else "NO",
                decision=record["docverify"]["filter_decision"],
                failure=record["docverify"].get("failure_taxonomy"),
                corr=expected.get("corruption_type"),
                seed=record["seed_id"],
                task=record["task_type"],
                ref=str(record["reference_answer"]).replace("|", "\\|"),
                final=str(record["final_answer"]).replace("|", "\\|"),
            )
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build and evaluate H3 negative-control corrupted trajectories.")
    parser.add_argument("--source-rollout-dir", default="data/h2/rollouts_v4")
    parser.add_argument("--negative-rollout-dir", default="data/h3/negative_v4/corrupted_rollouts")
    parser.add_argument("--out-dir", default="data/h3/negative_v4")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--include-missing-evidence", action="store_true")
    parser.add_argument("--include-extended-corruptions", action="store_true")
    parser.add_argument("--include-natural-like-corruptions", action="store_true")
    parser.add_argument("--max-per-type", type=int, default=None)
    args = parser.parse_args()

    build_summary = build_negative_rollouts(
        source_rollout_dir=Path(args.source_rollout_dir),
        out_rollout_dir=Path(args.negative_rollout_dir),
        include_missing_evidence=args.include_missing_evidence,
        include_extended_corruptions=args.include_extended_corruptions,
        include_natural_like_corruptions=args.include_natural_like_corruptions,
        max_per_type=args.max_per_type,
    )
    review = evaluate_negative(Path(args.negative_rollout_dir), Path(args.out_dir), top_k=args.top_k)
    summary = {
        "build": build_summary,
        "negative_eval": review["negative_eval"],
    }
    _write_json(Path(args.out_dir) / "summary.json", summary)
    print(json.dumps(summary["negative_eval"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
