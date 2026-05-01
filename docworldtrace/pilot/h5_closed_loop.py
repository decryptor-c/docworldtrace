from __future__ import annotations

import argparse
import gc
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple

import torch

from ..docenv import DocEnv
from .h2_eval import _score_rollout
from .h2_rollout import (
    TERMINAL_ACTIONS,
    extract_json_object,
    normalize_action_call,
    resolve_pdf_path,
)
from .h5_qwen_eval import _first_device, _render_prompt, load_model_and_processor
from .h5_qwen_sft import _resolve_template_style
from .h5_sft import _compact_observation, _task_prompt, _tool_schema_text


def _display_path(path: str | Path) -> str:
    path_obj = Path(path).expanduser()
    try:
        return str(path_obj.resolve().relative_to(Path.cwd().resolve()))
    except (OSError, ValueError):
        return str(path_obj)


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing JSONL file: {path}")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    items = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(item, ensure_ascii=False) for item in items) + ("\n" if items else ""),
        encoding="utf-8",
    )


def load_eval_seed_ids(sft_dir: str, split_name: str) -> List[str]:
    sft_path = Path(sft_dir)
    split_path = sft_path / "seed_split.jsonl"
    if split_path.exists():
        rows = _load_jsonl(split_path)
        return sorted(row["seed_id"] for row in rows if row.get("split") == split_name)

    fallback = sft_path / "trajectory_eval.jsonl"
    rows = _load_jsonl(fallback)
    return sorted({row["seed_id"] for row in rows})


def load_seed_map(rollout_dir: str, seed_file: str | None = None) -> Dict[str, Dict[str, Any]]:
    seeds: Dict[str, Dict[str, Any]] = {}
    if seed_file:
        for row in _load_jsonl(Path(seed_file)):
            seeds.setdefault(row["seed_id"], row)
    for path in sorted(Path(rollout_dir).glob("*/*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        seed = payload.get("seed") or {}
        if seed.get("seed_id"):
            seeds.setdefault(seed["seed_id"], seed)
    if not seeds:
        raise SystemExit(f"No seeds found from seed_file={seed_file} or rollout_dir={rollout_dir}")
    return seeds


def build_closed_loop_messages(seed: Dict[str, Any]) -> List[Dict[str, str]]:
    return [
        {
            "role": "system",
            "content": "You are a document ReAct agent.\n" + _tool_schema_text(),
        },
        {
            "role": "user",
            "content": _task_prompt(seed) + "\nReturn the next action as JSON.",
        },
    ]


def _generate_action(
    model: Any,
    processor: Any,
    tokenizer: Any,
    style: str,
    messages: Sequence[Dict[str, Any]],
    max_length: int,
    max_new_tokens: int,
    device: torch.device,
) -> str:
    prompt = _render_prompt(processor, messages, style)
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=max_length,
        add_special_tokens=False,
    )
    inputs = {key: value.to(device) for key, value in inputs.items()}
    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )
    generated_ids = output_ids[0, inputs["input_ids"].shape[1] :]
    return tokenizer.decode(generated_ids, skip_special_tokens=True)


def rollout_seed_with_model(
    seed: Dict[str, Any],
    adapter_name: str,
    adapter_path: str,
    model: Any,
    processor: Any,
    max_steps: int,
    max_length: int,
    max_new_tokens: int,
    pdf_cache: Dict[str, DocEnv],
) -> Dict[str, Any]:
    pdf_path = resolve_pdf_path(seed["pdf_path"])
    env = pdf_cache.setdefault(pdf_path, DocEnv.from_pdf(pdf_path))
    tokenizer = processor.tokenizer if hasattr(processor, "tokenizer") else processor
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    style = _resolve_template_style(processor, build_closed_loop_messages(seed))
    device = _first_device(model)

    messages = build_closed_loop_messages(seed)
    trajectory: List[Dict[str, Any]] = []
    status = "budget_exhausted"
    final_action = None
    final_answer = None

    for step in range(1, max_steps + 1):
        raw_text = _generate_action(
            model=model,
            processor=processor,
            tokenizer=tokenizer,
            style=style,
            messages=messages,
            max_length=max_length,
            max_new_tokens=max_new_tokens,
            device=device,
        )
        step_record: Dict[str, Any] = {
            "step": step,
            "raw_model_output": raw_text,
        }
        try:
            parsed = extract_json_object(raw_text)
            thought = str(parsed.get("thought", "")).strip()
            action_name = str(parsed.get("action", "")).strip()
            normalized_action, normalized_input = normalize_action_call(action_name, parsed.get("action_input", {}))
            observation = env.execute(normalized_action, **normalized_input)
            step_record.update(
                {
                    "thought": thought,
                    "action": normalized_action,
                    "action_input": normalized_input,
                    "observation": observation,
                    "format_valid": True,
                    "execution_valid": True,
                }
            )
            trajectory.append(step_record)
            normalized_json = json.dumps(
                {
                    "thought": thought,
                    "action": normalized_action,
                    "action_input": normalized_input,
                },
                ensure_ascii=False,
            )
            messages.append({"role": "assistant", "content": normalized_json})
            messages.append(
                {
                    "role": "user",
                    "content": "Observation:\n" + _compact_observation(step_record) + "\nReturn the next action as JSON.",
                }
            )
            if normalized_action in TERMINAL_ACTIONS:
                status = "completed"
                final_action = normalized_action
                if normalized_action == "answer":
                    final_answer = normalized_input.get("text", "")
                else:
                    final_answer = normalized_input.get("reason", "")
                break
        except Exception as exc:
            step_record.update(
                {
                    "format_valid": False,
                    "execution_valid": False,
                    "error": str(exc),
                }
            )
            trajectory.append(step_record)
            status = "format_error"
            break

    tool_sequence = [item.get("action") for item in trajectory if item.get("action")]
    nonterminal_tools = [action for action in tool_sequence if action not in TERMINAL_ACTIONS]
    return {
        "seed": seed,
        "teacher": {
            "name": adapter_name,
            "model": "Qwen3-VL-8B-Instruct",
            "adapter_path": _display_path(adapter_path),
        },
        "student": {
            "name": adapter_name,
            "adapter_path": _display_path(adapter_path),
        },
        "status": status,
        "trajectory": trajectory,
        "tool_sequence": tool_sequence,
        "final_action": final_action,
        "final_answer": final_answer,
        "raw_usage": [],
        "metrics": {
            "format_compliant": status != "format_error" and all(item.get("format_valid") for item in trajectory),
            "terminated_normally": status == "completed" and final_action in TERMINAL_ACTIONS,
            "step_count": len(trajectory),
            "used_verify": "verify" in tool_sequence,
            "used_refuse": final_action == "refuse",
            "direct_answer": bool(final_action in TERMINAL_ACTIONS and not nonterminal_tools),
        },
    }


def _required_tools_covered(seed: Dict[str, Any], tool_sequence: Sequence[str]) -> bool:
    required = [tool for tool in seed.get("required_tools", []) if tool not in TERMINAL_ACTIONS]
    return all(tool in tool_sequence for tool in required)


def _is_subsequence(pattern: Sequence[str], sequence: Sequence[str]) -> bool:
    if not pattern:
        return False
    start = 0
    for expected in pattern:
        try:
            index = sequence.index(expected, start)
        except ValueError:
            return False
        start = index + 1
    return True


def _acceptable_path_matched(seed: Dict[str, Any], tool_sequence: Sequence[str]) -> bool:
    acceptable_paths = seed.get("acceptable_paths") or []
    if not acceptable_paths:
        return _required_tools_covered(seed, tool_sequence)
    return any(_is_subsequence(path, tool_sequence) for path in acceptable_paths)


def _summarize_scores(items: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    total = len(items)
    if not total:
        return {
            "count": 0,
            "format_compliance_rate": 0.0,
            "proper_termination_rate": 0.0,
            "answer_correct_adjusted_rate": 0.0,
            "strict_answer_correct_rate": 0.0,
            "mean_answer_f1": 0.0,
            "avg_steps": 0.0,
            "direct_answer_rate": 0.0,
            "nonterminal_tool_use_rate": 0.0,
            "required_tool_coverage_rate": 0.0,
            "acceptable_path_rate": 0.0,
        }
    return {
        "count": total,
        "format_compliance_rate": round(sum(int(item["format_compliant"]) for item in items) / total, 4),
        "proper_termination_rate": round(sum(int(item["terminated_normally"]) for item in items) / total, 4),
        "answer_correct_adjusted_rate": round(sum(int(item["answer_correct_adjusted"]) for item in items) / total, 4),
        "strict_answer_correct_rate": round(sum(int(item["answer_correct"]) for item in items) / total, 4),
        "mean_answer_f1": round(sum(float(item["answer_f1"]) for item in items) / total, 4),
        "avg_steps": round(sum(int(item["step_count"]) for item in items) / total, 4),
        "direct_answer_rate": round(sum(int(item["direct_answer"]) for item in items) / total, 4),
        "nonterminal_tool_use_rate": round(
            sum(int(any(action not in TERMINAL_ACTIONS for action in item["tool_sequence"])) for item in items) / total,
            4,
        ),
        "required_tool_coverage_rate": round(sum(int(item["required_tools_covered"]) for item in items) / total, 4),
        "acceptable_path_rate": round(sum(int(item["acceptable_path_matched"]) for item in items) / total, 4),
    }


def evaluate_closed_loop_records(records: Sequence[Dict[str, Any]], out_dir: Path) -> Dict[str, Any]:
    scores: List[Dict[str, Any]] = []
    for record in records:
        score = _score_rollout(record)
        score["adapter"] = record["teacher"]["name"]
        score["tool_sequence"] = record.get("tool_sequence", [])
        score["required_tools_covered"] = _required_tools_covered(record["seed"], record.get("tool_sequence", []))
        score["acceptable_path_matched"] = _acceptable_path_matched(record["seed"], record.get("tool_sequence", []))
        score["file"] = record.get("_file")
        scores.append(score)

    by_adapter: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    by_task: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for score in scores:
        by_adapter[score["adapter"]].append(score)
        by_task[score["task_type"]].append(score)

    summary = {
        "out_dir": _display_path(out_dir),
        "overall": _summarize_scores(scores),
        "by_adapter": {adapter: _summarize_scores(items) for adapter, items in sorted(by_adapter.items())},
        "by_task_type": {task: _summarize_scores(items) for task, items in sorted(by_task.items())},
        "failure_categories": dict(Counter(score["failure_category"] for score in scores)),
        "action_distribution": dict(Counter(action for score in scores for action in score["tool_sequence"])),
        "records": scores,
    }
    adapters = summary["by_adapter"]
    if "trajectory" in adapters and "answer_only" in adapters:
        trajectory = adapters["trajectory"]
        answer_only = adapters["answer_only"]
        summary["trajectory_minus_answer_only"] = {
            "answer_correct_adjusted_rate": round(
                trajectory["answer_correct_adjusted_rate"] - answer_only["answer_correct_adjusted_rate"], 4
            ),
            "nonterminal_tool_use_rate": round(
                trajectory["nonterminal_tool_use_rate"] - answer_only["nonterminal_tool_use_rate"], 4
            ),
            "direct_answer_rate": round(trajectory["direct_answer_rate"] - answer_only["direct_answer_rate"], 4),
            "required_tool_coverage_rate": round(
                trajectory["required_tool_coverage_rate"] - answer_only["required_tool_coverage_rate"], 4
            ),
            "acceptable_path_rate": round(trajectory["acceptable_path_rate"] - answer_only["acceptable_path_rate"], 4),
        }
        summary["closed_loop_h5_passed"] = bool(
            trajectory["format_compliance_rate"] >= 0.9
            and trajectory["proper_termination_rate"] >= 0.8
            and trajectory["nonterminal_tool_use_rate"] > answer_only["nonterminal_tool_use_rate"]
            and trajectory["acceptable_path_rate"] > answer_only["acceptable_path_rate"]
        )
    else:
        summary["closed_loop_h5_passed"] = None
    return summary


def write_markdown(path: Path, summary: Dict[str, Any]) -> None:
    lines = [
        "# H5 Closed-Loop DocEnv Evaluation",
        "",
        f"- Output dir: `{summary['out_dir']}`",
        f"- Closed-loop H5 passed: `{summary['closed_loop_h5_passed']}`",
        "",
        "## Overall",
        "",
        "| Metric | Value |",
        "|---|---:|",
    ]
    for key, value in summary["overall"].items():
        lines.append(f"| `{key}` | `{value}` |")

    lines.extend(["", "## By Adapter", "", "| Adapter | Count | Adjusted Correct | Non-terminal Tool Use | Required Tool Coverage | Acceptable Path | Direct Answer | Termination |", "|---|---:|---:|---:|---:|---:|---:|---:|"])
    for adapter, stats in summary["by_adapter"].items():
        lines.append(
            f"| `{adapter}` | {stats['count']} | {stats['answer_correct_adjusted_rate']:.2%} | "
            f"{stats['nonterminal_tool_use_rate']:.2%} | {stats['required_tool_coverage_rate']:.2%} | "
            f"{stats['acceptable_path_rate']:.2%} | {stats['direct_answer_rate']:.2%} | "
            f"{stats['proper_termination_rate']:.2%} |"
        )

    if summary.get("trajectory_minus_answer_only"):
        lines.extend(["", "## Trajectory Minus Answer-Only", "", "| Metric | Delta |", "|---|---:|"])
        for key, value in summary["trajectory_minus_answer_only"].items():
            lines.append(f"| `{key}` | `{value:+.2%}` |")

    lines.extend(["", "## By Task Type", "", "| Task Type | Count | Adjusted Correct | Required Tool Coverage | Acceptable Path | Avg Steps |", "|---|---:|---:|---:|---:|---:|"])
    for task_type, stats in summary["by_task_type"].items():
        lines.append(
            f"| `{task_type}` | {stats['count']} | {stats['answer_correct_adjusted_rate']:.2%} | "
            f"{stats['required_tool_coverage_rate']:.2%} | {stats['acceptable_path_rate']:.2%} | "
            f"{stats['avg_steps']} |"
        )

    lines.extend(["", "## Failure Categories", ""])
    for category, count in sorted(summary["failure_categories"].items()):
        lines.append(f"- `{category}`: `{count}`")

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- This is the H5 closed-loop check: the adapter must generate actions, DocEnv executes them, and the next model call receives real observations.",
            "- The main comparison is `trajectory` vs `answer_only` on non-terminal tool use and required tool coverage.",
            "- Passing this check is stronger than next-action teacher-forcing eval, but it is still a pilot-scale result because the held-out seed set is small.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _parse_adapter_specs(values: Sequence[str]) -> List[Tuple[str, str]]:
    specs: List[Tuple[str, str]] = []
    for value in values:
        if "=" not in value:
            raise ValueError(f"Adapter spec must be name=path, got: {value}")
        name, path = value.split("=", 1)
        name = name.strip()
        path = path.strip()
        if not name or not path:
            raise ValueError(f"Invalid adapter spec: {value}")
        specs.append((name, path))
    return specs


def run_closed_loop(args: argparse.Namespace) -> Dict[str, Any]:
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    seed_ids = load_eval_seed_ids(args.sft_dir, args.split)
    if args.limit:
        seed_ids = seed_ids[: args.limit]
    seed_map = load_seed_map(args.rollout_dir, args.seed_file or None)
    missing = [seed_id for seed_id in seed_ids if seed_id not in seed_map]
    if missing:
        raise SystemExit(f"Missing seed definitions for {len(missing)} eval seeds: {missing[:10]}")
    seeds = [seed_map[seed_id] for seed_id in seed_ids]
    adapter_specs = _parse_adapter_specs(args.adapter)

    all_records: List[Dict[str, Any]] = []
    pdf_cache: Dict[str, DocEnv] = {}
    for adapter_name, adapter_path in adapter_specs:
        adapter_dir = out_dir / adapter_name
        adapter_dir.mkdir(parents=True, exist_ok=True)
        model, processor = load_model_and_processor(
            model_or_adapter=adapter_path,
            base_model=args.base_model,
            dtype=args.dtype,
            device_map=args.device_map,
        )
        for seed in seeds:
            record = rollout_seed_with_model(
                seed=seed,
                adapter_name=adapter_name,
                adapter_path=adapter_path,
                model=model,
                processor=processor,
                max_steps=args.max_steps,
                max_length=args.max_length,
                max_new_tokens=args.max_new_tokens,
                pdf_cache=pdf_cache,
            )
            record_path = adapter_dir / f"{seed['seed_id']}.json"
            record["_file"] = _display_path(record_path)
            record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            all_records.append(record)
            print(
                json.dumps(
                    {
                        "adapter": adapter_name,
                        "seed_id": seed["seed_id"],
                        "status": record["status"],
                        "tool_sequence": record["tool_sequence"],
                        "final_action": record["final_action"],
                        "final_answer": record["final_answer"],
                    },
                    ensure_ascii=False,
                ),
                flush=True,
            )
        del model
        del processor
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    summary = evaluate_closed_loop_records(all_records, out_dir)
    (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _write_jsonl(out_dir / "records.jsonl", summary["records"])
    write_markdown(out_dir / "summary.md", summary)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Run H5 closed-loop Qwen3-VL adapters inside DocEnv.")
    parser.add_argument("--base-model", required=True, help="Base Qwen3-VL model path")
    parser.add_argument(
        "--adapter",
        action="append",
        required=True,
        help="Adapter spec as name=path. Repeat for answer_only and trajectory adapters.",
    )
    parser.add_argument("--sft-dir", default="data/h5/sft_diverse_v2", help="H5 SFT data directory with seed_split.jsonl")
    parser.add_argument("--rollout-dir", default="data/h2/rollouts_diverse_v2", help="Rollout dir used to recover seed metadata")
    parser.add_argument("--seed-file", default="", help="Optional seed JSONL file")
    parser.add_argument("--split", default="eval", choices=["train", "eval"], help="Seed split to evaluate")
    parser.add_argument("--out-dir", default="data/h5/closed_loop_diverse_v2")
    parser.add_argument("--max-steps", type=int, default=8)
    parser.add_argument("--max-length", type=int, default=4096)
    parser.add_argument("--max-new-tokens", type=int, default=256)
    parser.add_argument("--dtype", choices=["auto", "bf16", "fp16", "fp32"], default="bf16")
    parser.add_argument("--device-map", default="auto")
    parser.add_argument("--limit", type=int, default=0, help="Optional number of eval seeds for smoke tests")
    args = parser.parse_args()

    summary = run_closed_loop(args)
    printable = {key: value for key, value in summary.items() if key != "records"}
    print(json.dumps(printable, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
