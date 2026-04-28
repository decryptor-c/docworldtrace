# H5 SFT Data Preparation

- Rollout dir: `data/h2/rollouts_v5`
- DocVerify++ source: `data/h3/docverify_plus_v5/docverify_review.json`
- Output dir: `data/h5/sft_v5`
- Kept rollout count: `116`
- Unique seed count: `20`
- Split rollout counts: `{'train': 83, 'eval': 33}`

## Dataset Counts

- `answer_only_train.jsonl`: `83`
- `answer_only_eval.jsonl`: `33`
- `trajectory_train.jsonl`: `233`
- `trajectory_eval.jsonl`: `94`

## Supervision Signal

- Answer-only train terminal target rate: `100.00%`
- Trajectory train non-terminal target rate: `64.38%`
- Trajectory train core tool coverage: `['answer', 'compute', 'parse_table', 'read_page', 'refuse', 'search', 'verify']`

## Interpretation

- `answer_only_train.jsonl` supervises only terminal answer/refuse behavior.
- `trajectory_train.jsonl` supervises next-action ReAct behavior, including evidence tools before terminal actions.
- A real H5 SFT run should train identical base models on the two train files and evaluate on the corresponding eval split.
