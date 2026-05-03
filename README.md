# DocWorldTrace

DocWorldTrace converts static PDF documents into an interactive document-agent environment, then uses the environment to generate, verify, diversify, and train multi-step document tool trajectories.

The current repository contains the pilot pipeline from H1 to H5:

```text
H1: PDF -> DocEnv tool feasibility
H2: teacher model rollout generation
H3: DocVerify++ trajectory verification/filtering
H4: trajectory diversity analysis
H5: Qwen3-VL answer-only vs trajectory SFT
```

## Quick Links

| File | Purpose |
|---|---|
| `docs/reports/h1_h4_experiment_summary.md` | Main H1-H5 technical summary with experiment results |
| `docs/reports/h1_h5_presentation_report.md` | Presentation-oriented report focused on results, data, and examples |
| `docs/reports/h5_experiment_report.md` | Standalone H5 Qwen3-VL SFT report |
| `docs/reports/h5_closed_loop_trajectory_comparison.md` | H5 answer-only vs trajectory closed-loop example comparison |
| `docs/reports/h1_h4_analysis_report.md` | Analysis report and limitations |
| `REPOSITORY_STRUCTURE.md` | Repository layout and artifact map |

## Repository Layout

| Path | Contents |
|---|---|
| `docworldtrace/` | Core DocEnv, search, verification, and safe compute implementation |
| `docworldtrace/pilot/` | H1-H5 pilot experiment modules |
| `docs/research_plan/` | Research plan and experiment design notes |
| `docs/reports/` | Shared experiment summaries and presentation reports |
| `related_work/` | Literature review and proposal materials |
| `scripts/` | Reproducible shell/Python entrypoints |
| `data/` | Seeds, rollouts, evaluation summaries, reports, and local PDFs |
| `artifacts/` | Rendered pages and crop images used by DocEnv/manual review |
| `tests/` | Smoke and unit tests |
| `pilot_exp1/`, `pilot_h2/` | Early pilot templates/configs |

## Environment

Create and activate a local virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-server.txt
```

For H5 Qwen3-VL SFT, install the separate training dependencies:

```bash
bash scripts/setup_h5_qwen_sft_env.sh
```

If the server needs to install a CUDA torch build:

```bash
H5_INSTALL_TORCH=1 H5_TORCH_INDEX_URL=https://download.pytorch.org/whl/cu121 \
  bash scripts/setup_h5_qwen_sft_env.sh
```

## Main Workflows

### H1-H4

See:

```text
scripts/README_h1_h4.md
```

Typical entrypoints:

```bash
bash scripts/run_h1_h4_pilot.sh
bash scripts/run_h2_h4_v5_pipeline.sh
H2_REPEATS=1 bash scripts/run_prepared_h4_pipeline.sh
```

### H5

See:

```text
scripts/README_h5_qwen3_vl.md
```

Typical server commands:

```bash
CUDA_VISIBLE_DEVICES=1 H5_LOAD_IN_4BIT=1 bash scripts/run_h5_qwen3_vl_sft.sh
CUDA_VISIBLE_DEVICES=1 bash scripts/run_h5_qwen3_vl_closed_loop.sh
```

## Current Key Results

| Stage | Main Result |
|---|---|
| H1 | 5 PDFs, 50 deterministic tool calls, 100% success |
| H2 | Teacher rollouts produce multi-step DocEnv trajectories |
| H3 | DocVerify++ validates/filter trajectories into auditable data |
| H4 | Trajectories cover text lookup, table lookup, cross-page, verification, refusal, and numeric computation |
| H5 | Trajectory SFT outperforms answer-only SFT in next-action and closed-loop evaluation |

H5 headline:

```text
Next-action action match: 38% -> 98%
Closed-loop adjusted correct: 33.33% -> 83.33%
Closed-loop non-terminal tool use: 0% -> 100%
```

## Data And Artifact Policy

- `.env*`, API keys, model weights, logs, and training `runs/` are local-only.
- `models/` is intentionally ignored; download Qwen3-VL with `scripts/download_qwen3_vl_8b_modelscope.sh`.
- Large/generated experiment outputs should be reviewed before pushing.
- Current summary/report files are small and intended for sharing.

## Tests

```bash
pytest
```

If `pytest` is unavailable:

```bash
python -m pytest
```
