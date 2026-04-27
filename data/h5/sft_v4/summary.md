# H5 SFT Data Preparation

- Rollout dir: `data/h2/rollouts_v4`
- DocVerify++ source: `data/h3/docverify_plus_v4/docverify_review.json`
- Output dir: `data/h5/sft_v4`
- Kept rollout count: `80`
- Unique seed count: `20`
- Split rollout counts: `{'train': 56, 'eval': 24}`

## Dataset Counts

- `answer_only_train.jsonl`: `56`
- `answer_only_eval.jsonl`: `24`
- `trajectory_train.jsonl`: `162`
- `trajectory_eval.jsonl`: `72`

## Supervision Signal

- Answer-only train terminal target rate: `100.00%`
- Trajectory train non-terminal target rate: `65.43%`
- Trajectory train core tool coverage: `['answer', 'compute', 'parse_table', 'read_page', 'refuse', 'search', 'verify']`

## Interpretation

- `answer_only_train.jsonl` supervises only terminal answer/refuse behavior.
- `trajectory_train.jsonl` supervises next-action ReAct behavior, including evidence tools before terminal actions.
- A real H5 SFT run should train identical base models on the two train files and evaluate on the corresponding eval split.
