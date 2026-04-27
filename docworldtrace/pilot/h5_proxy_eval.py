from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


def _load(path: str) -> Dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _overall(path: str) -> Dict[str, Any]:
    payload = _load(path)
    return payload.get("overall", payload)


def _pct(value: float) -> str:
    return f"{value:.2%}"


def _delta(tool: float, baseline: float) -> float:
    return round(tool - baseline, 4)


def evaluate_h5_proxy(
    sft_summary_path: str,
    no_tool_eval_path: str,
    tool_eval_path: str,
    path_review_path: str,
    docverify_path: str,
    out_dir: str,
) -> Dict[str, Any]:
    sft = _load(sft_summary_path)
    no_tool = _overall(no_tool_eval_path)
    tool = _overall(tool_eval_path)
    path_review = _overall(path_review_path)
    docverify = _overall(docverify_path)

    trajectory_train = sft["trajectory_train"]
    answer_only_train = sft["answer_only_train"]
    deltas = {
        "adjusted_answer_correct_rate": _delta(
            tool.get("answer_correct_adjusted_rate", 0.0),
            no_tool.get("answer_correct_adjusted_rate", 0.0),
        ),
        "direct_answer_rate": _delta(tool.get("direct_answer_rate", 0.0), no_tool.get("direct_answer_rate", 0.0)),
        "avg_steps": _delta(tool.get("avg_steps", 0.0), no_tool.get("avg_steps", 0.0)),
        "verify_usage_rate": _delta(tool.get("verify_usage_rate", 0.0), no_tool.get("verify_usage_rate", 0.0)),
    }

    criteria = {
        "sft_files_present": all(
            sft["dataset_counts"].get(name, 0) > 0
            for name in ["answer_only_train", "answer_only_eval", "trajectory_train", "trajectory_eval"]
        ),
        "trajectory_has_nonterminal_supervision": trajectory_train.get("nonterminal_target_rate", 0.0) >= 0.5,
        "trajectory_covers_core_tools": len(trajectory_train.get("core_tool_coverage", [])) >= 7,
        "docverify_keep_rate_ok": docverify.get("keep_rate", 0.0) >= 0.9,
        "acceptable_path_rate_ok": path_review.get("acceptable_path_ok_rate", 0.0) >= 0.9,
        "proxy_tool_use_improves_over_answer_only": tool.get("direct_answer_rate", 1.0) < no_tool.get("direct_answer_rate", 0.0),
        "proxy_accuracy_improves_over_answer_only": tool.get("answer_correct_adjusted_rate", 0.0)
        >= no_tool.get("answer_correct_adjusted_rate", 0.0) + 0.05,
    }
    h5_proxy_passed = all(criteria.values())

    summary = {
        "sft_summary": sft_summary_path,
        "no_tool_eval": no_tool_eval_path,
        "tool_eval": tool_eval_path,
        "path_review": path_review_path,
        "docverify": docverify_path,
        "h5_proxy_passed": h5_proxy_passed,
        "criteria": criteria,
        "dataset_counts": sft["dataset_counts"],
        "answer_only_train_signal": {
            "terminal_target_rate": answer_only_train.get("terminal_target_rate", 0.0),
            "nonterminal_target_rate": answer_only_train.get("nonterminal_target_rate", 0.0),
            "core_tool_coverage": answer_only_train.get("core_tool_coverage", []),
        },
        "trajectory_train_signal": {
            "terminal_target_rate": trajectory_train.get("terminal_target_rate", 0.0),
            "nonterminal_target_rate": trajectory_train.get("nonterminal_target_rate", 0.0),
            "core_tool_coverage": trajectory_train.get("core_tool_coverage", []),
            "target_action_distribution": trajectory_train.get("target_action_distribution", {}),
        },
        "no_tool_overall": no_tool,
        "docenv_agent_overall": tool,
        "path_overall": path_review,
        "docverify_overall": docverify,
        "docenv_minus_no_tool": deltas,
        "interpretation": (
            "This is an H5 proxy/readiness result, not a completed model fine-tuning result. "
            "It verifies that the SFT files exist, trajectory supervision contains non-terminal tool actions, "
            "and the observed DocEnv-agent behavior dominates the no-tool answer-only control."
        ),
    }

    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    (out_path / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(out_path / "summary.md", summary)
    return summary


def write_markdown(path: Path, summary: Dict[str, Any]) -> None:
    lines: List[str] = [
        "# H5 Pilot Proxy Evaluation",
        "",
        f"- H5 proxy passed: `{summary['h5_proxy_passed']}`",
        "",
        "## Criteria",
        "",
    ]
    for key, value in summary["criteria"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines.extend(
        [
            "",
            "## Dataset Counts",
            "",
        ]
    )
    for key, value in summary["dataset_counts"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines.extend(
        [
            "",
            "## Supervision Signal",
            "",
            f"- Answer-only terminal target rate: `{_pct(summary['answer_only_train_signal']['terminal_target_rate'])}`",
            f"- Trajectory non-terminal target rate: `{_pct(summary['trajectory_train_signal']['nonterminal_target_rate'])}`",
            f"- Trajectory core tool coverage: `{summary['trajectory_train_signal']['core_tool_coverage']}`",
            f"- Trajectory target action distribution: `{summary['trajectory_train_signal']['target_action_distribution']}`",
            "",
            "## Proxy Control Comparison",
            "",
            "| Metric | No-tool answer-only control | DocEnv trajectory agent | Delta |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    no_tool = summary["no_tool_overall"]
    tool = summary["docenv_agent_overall"]
    deltas = summary["docenv_minus_no_tool"]
    for metric in [
        "answer_correct_adjusted_rate",
        "direct_answer_rate",
        "avg_steps",
        "verify_usage_rate",
        "refuse_usage_rate",
    ]:
        left = no_tool.get(metric, 0.0)
        right = tool.get(metric, 0.0)
        delta = deltas.get(metric, right - left)
        fmt = _pct if isinstance(left, float) and 0 <= left <= 1 and metric != "avg_steps" else lambda x: f"{x:.4g}"
        lines.append(f"| `{metric}` | {fmt(left)} | {fmt(right)} | {fmt(delta)} |")

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- This report is a pilot proxy/readiness check, not a completed SFT training result.",
            "- The real H5 claim still requires training the same base model on answer-only vs trajectory JSONL files.",
            "- Passing this proxy means the data and behavior contrast are strong enough to justify the actual SFT run.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate H5 SFT readiness and answer-only vs trajectory proxy contrast.")
    parser.add_argument("--sft-summary", default="data/h5/sft_v4/summary.json")
    parser.add_argument("--no-tool-eval", default="data/h2/eval_no_tool_v3/summary.json")
    parser.add_argument("--tool-eval", default="data/h2/eval_v4/summary.json")
    parser.add_argument("--path-review", default="data/h2/eval_v4_path/path_review.json")
    parser.add_argument("--docverify", default="data/h3/docverify_plus_v4/docverify_review.json")
    parser.add_argument("--out-dir", default="data/h5/eval_v4")
    args = parser.parse_args()

    summary = evaluate_h5_proxy(
        sft_summary_path=args.sft_summary,
        no_tool_eval_path=args.no_tool_eval,
        tool_eval_path=args.tool_eval,
        path_review_path=args.path_review,
        docverify_path=args.docverify,
        out_dir=args.out_dir,
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
