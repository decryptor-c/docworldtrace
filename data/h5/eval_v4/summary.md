# H5 Pilot Proxy Evaluation

- H5 proxy passed: `True`

## Criteria

- `sft_files_present`: `True`
- `trajectory_has_nonterminal_supervision`: `True`
- `trajectory_covers_core_tools`: `True`
- `docverify_keep_rate_ok`: `True`
- `acceptable_path_rate_ok`: `True`
- `proxy_tool_use_improves_over_answer_only`: `True`
- `proxy_accuracy_improves_over_answer_only`: `True`

## Dataset Counts

- `answer_only_train`: `56`
- `answer_only_eval`: `24`
- `trajectory_train`: `162`
- `trajectory_eval`: `72`

## Supervision Signal

- Answer-only terminal target rate: `100.00%`
- Trajectory non-terminal target rate: `65.43%`
- Trajectory core tool coverage: `['answer', 'compute', 'parse_table', 'read_page', 'refuse', 'search', 'verify']`
- Trajectory target action distribution: `{'search': 27, 'read_page': 55, 'answer': 44, 'refuse': 12, 'parse_table': 10, 'compute': 8, 'verify': 4, 'crop': 2}`

## Proxy Control Comparison

| Metric | No-tool answer-only control | DocEnv trajectory agent | Delta |
| --- | ---: | ---: | ---: |
| `answer_correct_adjusted_rate` | 32.50% | 100.00% | 67.50% |
| `direct_answer_rate` | 100.00% | 0.00% | -100.00% |
| `avg_steps` | 1 | 2.925 | 1.925 |
| `verify_usage_rate` | 0.00% | 10.00% | 10.00% |
| `refuse_usage_rate` | 87.50% | 20.00% | -67.50% |

## Interpretation

- This report is a pilot proxy/readiness check, not a completed SFT training result.
- The real H5 claim still requires training the same base model on answer-only vs trajectory JSONL files.
- Passing this proxy means the data and behavior contrast are strong enough to justify the actual SFT run.
