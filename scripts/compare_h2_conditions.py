#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


METRICS = [
    "count",
    "format_compliance_rate",
    "proper_termination_rate",
    "answer_correct_rate",
    "answer_correct_adjusted_rate",
    "mean_answer_f1",
    "avg_steps",
    "verify_usage_rate",
    "refuse_usage_rate",
    "direct_answer_rate",
]


def _load(path: str) -> Dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return payload.get("overall", payload)


def _fmt(value: Any) -> str:
    if isinstance(value, float):
        if 0 <= value <= 1:
            return f"{value:.2%}"
        return f"{value:.4g}"
    return str(value)


def _delta(tool: Any, baseline: Any) -> str:
    if isinstance(tool, (int, float)) and isinstance(baseline, (int, float)):
        diff = tool - baseline
        if isinstance(tool, float) or isinstance(baseline, float):
            if -1 <= diff <= 1:
                return f"{diff:+.2%}"
            return f"{diff:+.4g}"
        return f"{diff:+d}"
    return ""


def _rows(baseline: Dict[str, Any], tool: Dict[str, Any]) -> List[str]:
    lines = ["| Metric | No-tool baseline | DocEnv-agent | Delta |", "| --- | ---: | ---: | ---: |"]
    for metric in METRICS:
        if metric not in baseline and metric not in tool:
            continue
        base_value = baseline.get(metric, "")
        tool_value = tool.get(metric, "")
        lines.append(f"| `{metric}` | {_fmt(base_value)} | {_fmt(tool_value)} | {_delta(tool_value, base_value)} |")
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare H2 no-tool baseline with DocEnv-agent evaluation summaries.")
    parser.add_argument("baseline_summary", help="No-tool baseline eval summary JSON")
    parser.add_argument("tool_summary", help="DocEnv-agent eval summary JSON")
    parser.add_argument("out_md", help="Output markdown report")
    args = parser.parse_args()

    baseline = _load(args.baseline_summary)
    tool = _load(args.tool_summary)
    out_path = Path(args.out_md)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# H2 Control Experiment Comparison",
        "",
        f"- No-tool baseline summary: `{args.baseline_summary}`",
        f"- DocEnv-agent summary: `{args.tool_summary}`",
        "",
        "## Overall Metrics",
        "",
        *_rows(baseline, tool),
        "",
        "## Interpretation Template",
        "",
        "- If DocEnv-agent has higher adjusted answer correctness, the tool environment improves answer reliability.",
        "- If DocEnv-agent has lower direct answer rate, the model is relying less on unsupported guessing.",
        "- If no-tool baseline has high refusal rate on answerable tasks, it indicates that document access is needed for these questions.",
        "- If no-tool baseline answers some tasks correctly, manually check whether the seed leaked enough information in the question.",
        "",
    ]
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Comparison written to {out_path}")


if __name__ == "__main__":
    main()
