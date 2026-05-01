# H5 Qwen3-VL SFT

This workflow trains two LoRA adapters from the same Qwen3-VL-8B-Instruct base model:

- `answer_only_adapter`: supervised only on terminal `answer/refuse` JSON.
- `trajectory_adapter`: supervised on next-action ReAct JSON, including document tools such as `search`, `read_page`, `parse_table`, `compute`, and `verify`.

The comparison is the H5 experiment: whether trajectory supervision teaches tool-use behavior beyond answer-only supervision.

## 1. Prepare Model

Download the model to the repository-local `models/` directory:

```bash
cd ~/DocWorldTrace
source .venv/bin/activate
bash scripts/download_qwen3_vl_8b_modelscope.sh
```

Expected default model path:

```text
models/Qwen3-VL-8B-Instruct
```

## 2. Install SFT Dependencies

If torch is already installed with the correct CUDA build:

```bash
cd ~/DocWorldTrace
source .venv/bin/activate
bash scripts/setup_h5_qwen_sft_env.sh
```

If torch is missing, install a CUDA 12.1 build first through the setup script:

```bash
H5_INSTALL_TORCH=1 H5_TORCH_INDEX_URL=https://download.pytorch.org/whl/cu121 \
  bash scripts/setup_h5_qwen_sft_env.sh
```

## 3. Run H5 SFT

Default diverse-v2 run:

```bash
cd ~/DocWorldTrace
source .venv/bin/activate
H5_LOAD_IN_4BIT=1 bash scripts/run_h5_qwen3_vl_sft.sh
```

If only physical GPU 1 is available, restrict the process to that GPU:

```bash
cd ~/DocWorldTrace
source .venv/bin/activate
CUDA_VISIBLE_DEVICES=1 H5_LOAD_IN_4BIT=1 bash scripts/run_h5_qwen3_vl_sft.sh
```

Inside the process, physical GPU 1 will appear as `cuda:0`; this is expected.

Default inputs:

```text
data/h2/rollouts_diverse_v2
data/h3/docverify_plus_diverse_v2/docverify_review.json
```

Default outputs:

```text
data/h5/sft_diverse_v2
runs/h5_qwen3_vl_diverse_v2
```

The current `docverify_plus_diverse_v2/docverify_review.json` artifact may be truncated after synchronization. The run script therefore defaults to `H5_KEEP_ALL=auto`: if the DocVerify JSON is valid, it uses keep decisions; if it is invalid, it builds H5 data with `--keep-all`. This is acceptable for the current diverse-v2 result because its readable DocVerify report marks all 162 trajectories as `keep`.

## 4. Useful Runtime Options

```bash
H5_MODEL_DIR=models/Qwen3-VL-8B-Instruct
H5_EPOCHS=2
H5_LR=2e-4
H5_BATCH_SIZE=1
H5_GRAD_ACCUM=8
H5_MAX_LENGTH=4096
H5_LOAD_IN_4BIT=1
H5_FORCE_TRAIN=1
H5_LIMIT_EVAL=20
```

For a quick smoke test:

```bash
H5_LOAD_IN_4BIT=1 H5_EPOCHS=0.05 H5_LIMIT_EVAL=10 \
  bash scripts/run_h5_qwen3_vl_sft.sh
```

For a full run without 4-bit quantization, use a large enough GPU and omit `H5_LOAD_IN_4BIT=1`.

## 5. Main Evaluation Signal

After training, inspect:

```text
runs/h5_qwen3_vl_diverse_v2/h5_qwen_eval_summary.json
```

The most important comparison is:

- `answer_only_adapter_on_trajectory_eval`: should mostly emit terminal `answer/refuse`.
- `trajectory_adapter_on_trajectory_eval`: should have higher valid JSON rate, action match rate, and non-terminal tool-action rate.

If the trajectory adapter generates `search/read_page/parse_table/compute/verify` on held-out trajectory prompts while the answer-only adapter does not, H5 has the expected behavioral signal.

## 6. Closed-Loop DocEnv Evaluation

The next-action eval above is teacher-forcing style: each sample already contains the previous gold observations. To test whether the trained adapter can actually interact with DocEnv, run the closed-loop evaluator:

```bash
cd ~/DocWorldTrace
source .venv/bin/activate
CUDA_VISIBLE_DEVICES=1 bash scripts/run_h5_qwen3_vl_closed_loop.sh
```

For a quick smoke test:

```bash
CUDA_VISIBLE_DEVICES=1 H5_CLOSED_LOOP_LIMIT=2 \
  bash scripts/run_h5_qwen3_vl_closed_loop.sh
```

Default inputs:

```text
models/Qwen3-VL-8B-Instruct
runs/h5_qwen3_vl_diverse_v2/answer_only_adapter
runs/h5_qwen3_vl_diverse_v2/trajectory_adapter
data/h5/sft_diverse_v2/seed_split.jsonl
data/h2/rollouts_diverse_v2
```

Default outputs:

```text
data/h5/closed_loop_diverse_v2/summary.md
data/h5/closed_loop_diverse_v2/summary.json
data/h5/closed_loop_diverse_v2/records.jsonl
logs/h5_closed_loop_*.log
```

The closed-loop evaluator runs both adapters on the held-out H5 eval seeds, executes each generated action in DocEnv, feeds the real observation back to the model, and compares final answers/refusals against the seed ground truth. The main signal is whether `trajectory_adapter` improves non-terminal tool use and required-tool coverage over `answer_only_adapter`.
