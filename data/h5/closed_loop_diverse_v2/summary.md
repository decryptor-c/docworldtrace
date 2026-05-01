# H5 Closed-Loop DocEnv Evaluation

- Output dir: `data/h5/closed_loop_diverse_v2`
- Closed-loop H5 passed: `True`

## Overall

| Metric | Value |
|---|---:|
| `count` | `12` |
| `format_compliance_rate` | `0.9167` |
| `proper_termination_rate` | `0.8333` |
| `answer_correct_adjusted_rate` | `0.5833` |
| `strict_answer_correct_rate` | `0.5833` |
| `mean_answer_f1` | `0.5985` |
| `avg_steps` | `2.3333` |
| `direct_answer_rate` | `0.4167` |
| `nonterminal_tool_use_rate` | `0.5` |
| `required_tool_coverage_rate` | `0.25` |
| `acceptable_path_rate` | `0.4167` |

## By Adapter

| Adapter | Count | Adjusted Correct | Non-terminal Tool Use | Required Tool Coverage | Acceptable Path | Direct Answer | Termination |
|---|---:|---:|---:|---:|---:|---:|---:|
| `answer_only` | 6 | 33.33% | 0.00% | 0.00% | 0.00% | 83.33% | 83.33% |
| `trajectory` | 6 | 83.33% | 100.00% | 50.00% | 83.33% | 0.00% | 83.33% |

## Trajectory Minus Answer-Only

| Metric | Delta |
|---|---:|
| `answer_correct_adjusted_rate` | `+50.00%` |
| `nonterminal_tool_use_rate` | `+100.00%` |
| `direct_answer_rate` | `-83.33%` |
| `required_tool_coverage_rate` | `+50.00%` |
| `acceptable_path_rate` | `+83.33%` |

## By Task Type

| Task Type | Count | Adjusted Correct | Required Tool Coverage | Acceptable Path | Avg Steps |
|---|---:|---:|---:|---:|---:|
| `cross_page` | 2 | 50.00% | 50.00% | 50.00% | 2.5 |
| `numeric_computation` | 2 | 50.00% | 50.00% | 50.00% | 2.0 |
| `table_lookup` | 2 | 50.00% | 0.00% | 50.00% | 1.5 |
| `text_lookup` | 2 | 50.00% | 50.00% | 50.00% | 1.5 |
| `unanswerable` | 2 | 50.00% | 0.00% | 0.00% | 4.5 |
| `verification` | 2 | 100.00% | 0.00% | 50.00% | 2.0 |

## Failure Categories

- `budget_exhausted`: `1`
- `format_error`: `1`
- `strict_correct`: `7`
- `wrong_answer`: `3`

## Interpretation

- This is the H5 closed-loop check: the adapter must generate actions, DocEnv executes them, and the next model call receives real observations.
- The main comparison is `trajectory` vs `answer_only` on non-terminal tool use and required tool coverage.
- Passing this check is stronger than next-action teacher-forcing eval, but it is still a pilot-scale result because the held-out seed set is small.
