# H5 SFT Data Preparation

- Rollout dir: `data/h2/rollouts_diverse_v2`
- DocVerify++ source: `None`
- Keep all rollouts: `True`
- Output dir: `data/h5/sft_diverse_v2`
- Kept rollout count: `162`
- Unique seed count: `54`
- Split rollout counts: `{'train': 144, 'eval': 18}`

## Dataset Counts

- `answer_only_train.jsonl`: `144`
- `answer_only_eval.jsonl`: `18`
- `trajectory_train.jsonl`: `427`
- `trajectory_eval.jsonl`: `50`

## Supervision Signal

- Answer-only train terminal target rate: `100.00%`
- Trajectory train non-terminal target rate: `66.28%`
- Trajectory train core tool coverage: `['answer', 'compute', 'parse_table', 'read_page', 'refuse', 'search', 'verify']`

## Interpretation

- `answer_only_train.jsonl` supervises only terminal answer/refuse behavior.
- `trajectory_train.jsonl` supervises next-action ReAct behavior, including evidence tools before terminal actions.
- A real H5 SFT run should train identical base models on the two train files and evaluate on the corresponding eval split.
