from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .h2_client import OpenAICompatibleClient, TeacherConfig, load_teacher_configs
from .h2_rollout import display_path, extract_json_object, load_seeds, teacher_public_metadata


def _baseline_messages(seed: Dict[str, Any]) -> List[Dict[str, str]]:
    task_payload = {
        "seed_id": seed["seed_id"],
        "doc_id": seed["doc_id"],
        "task_type": seed["task_type"],
        "answerable": seed["answerable"],
        "question": seed["question"],
    }
    return [
        {
            "role": "system",
            "content": (
                "You are a no-tool document-question baseline.\n"
                "You cannot inspect the PDF and cannot call tools. Answer only from the question text and general knowledge.\n"
                "If the question requires document evidence that is not available in the prompt, refuse briefly.\n"
                "Return exactly one JSON object with keys \"thought\", \"action\", and \"action_input\".\n"
                "The action must be either \"answer\" or \"refuse\".\n"
                "For answer, use action_input {\"text\": \"...\"}. For refuse, use action_input {\"reason\": \"...\"}.\n"
                "Do not include markdown fences."
            ),
        },
        {
            "role": "user",
            "content": (
                "No-tool baseline task:\n"
                + json.dumps(task_payload, ensure_ascii=False)
                + "\nReturn your final action as JSON."
            ),
        },
    ]


def _terminal_from_payload(payload: Dict[str, Any]) -> tuple[str, str]:
    action = str(payload.get("action", "")).strip().lower()
    action_input = payload.get("action_input") or {}
    if not isinstance(action_input, dict):
        action_input = {}
    if action == "answer":
        return "answer", str(action_input.get("text", action_input.get("answer", "")))
    if action == "refuse":
        return "refuse", str(action_input.get("reason", action_input.get("text", "Insufficient evidence")))
    raise ValueError(f"No-tool baseline must use answer/refuse, got: {action}")


def baseline_seed(seed: Dict[str, Any], teacher: TeacherConfig) -> Dict[str, Any]:
    client = OpenAICompatibleClient(teacher)
    messages = _baseline_messages(seed)
    response = client.chat(messages)
    raw_text = response["content"]
    raw_usage = [response.get("usage", {})]
    step_record: Dict[str, Any] = {
        "step": 1,
        "raw_model_output": raw_text,
    }

    try:
        parsed = extract_json_object(raw_text)
        thought = str(parsed.get("thought", "")).strip()
        final_action, final_answer = _terminal_from_payload(parsed)
        action_input = {"text": final_answer} if final_action == "answer" else {"reason": final_answer}
        step_record.update(
            {
                "thought": thought,
                "action": final_action,
                "action_input": action_input,
                "observation": {
                    "action": final_action,
                    "status": "success",
                    "result": action_input,
                    "provenance": {"page": None, "bbox": None, "element_type": "no_tool_baseline"},
                    "confidence": 0.0,
                    "cache_hit": False,
                },
                "format_valid": True,
                "execution_valid": True,
            }
        )
        status = "completed"
        trajectory = [step_record]
        tool_sequence = [final_action]
        format_compliant = True
        terminated_normally = True
    except Exception as exc:
        step_record.update(
            {
                "format_valid": False,
                "execution_valid": False,
                "error": str(exc),
            }
        )
        status = "format_error"
        trajectory = [step_record]
        tool_sequence = []
        final_action = None
        final_answer = None
        format_compliant = False
        terminated_normally = False

    return {
        "seed": seed,
        "teacher": teacher_public_metadata(teacher),
        "condition": "no_tool_baseline",
        "status": status,
        "trajectory": trajectory,
        "tool_sequence": tool_sequence,
        "final_action": final_action,
        "final_answer": final_answer,
        "raw_usage": raw_usage,
        "metrics": {
            "format_compliant": format_compliant,
            "terminated_normally": terminated_normally,
            "step_count": len(trajectory),
            "used_verify": False,
            "used_refuse": final_action == "refuse",
            "direct_answer": final_action in {"answer", "refuse"},
        },
    }


def error_baseline(seed: Dict[str, Any], teacher: TeacherConfig, error: str) -> Dict[str, Any]:
    return {
        "seed": seed,
        "teacher": teacher_public_metadata(teacher),
        "condition": "no_tool_baseline",
        "status": "teacher_error",
        "error": error,
        "trajectory": [],
        "tool_sequence": [],
        "final_action": None,
        "final_answer": None,
        "raw_usage": [],
        "metrics": {
            "format_compliant": False,
            "terminated_normally": False,
            "step_count": 0,
            "used_verify": False,
            "used_refuse": False,
            "direct_answer": False,
        },
    }


def run_baseline(
    seed_file: str,
    teacher_config_path: str,
    out_dir: str,
    repeats: int,
) -> Dict[str, Any]:
    seeds = load_seeds(seed_file)
    teachers = load_teacher_configs(teacher_config_path)
    out_root = Path(out_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    outputs: List[str] = []

    for teacher in teachers:
        teacher_dir = out_root / teacher.name
        teacher_dir.mkdir(parents=True, exist_ok=True)
        for seed in seeds:
            for run_index in range(1, repeats + 1):
                try:
                    rollout = baseline_seed(seed, teacher)
                except Exception as exc:
                    rollout = error_baseline(seed, teacher, str(exc))
                file_name = f"{seed['seed_id']}__run{run_index:02d}.json"
                path = teacher_dir / file_name
                path.write_text(json.dumps(rollout, ensure_ascii=False, indent=2), encoding="utf-8")
                outputs.append(display_path(str(path)))

    summary = {
        "condition": "no_tool_baseline",
        "seed_file": display_path(seed_file),
        "teacher_config_path": display_path(teacher_config_path),
        "out_dir": display_path(str(out_root)),
        "rollout_count": len(outputs),
        "files": outputs,
    }
    (out_root / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Run H2 no-tool baseline rollouts.")
    parser.add_argument("--seed-file", default="data/h2/seeds/pilot_seeds_v3.jsonl", help="Seed JSONL file")
    parser.add_argument("--teacher-config", default="data/h2/teachers.json", help="Teacher config JSON")
    parser.add_argument("--out-dir", default="data/h2/baseline_no_tool_v3", help="Output directory")
    parser.add_argument("--repeats", type=int, default=1, help="Number of rollouts per seed per teacher")
    args = parser.parse_args()

    summary = run_baseline(
        seed_file=args.seed_file,
        teacher_config_path=args.teacher_config,
        out_dir=args.out_dir,
        repeats=args.repeats,
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
