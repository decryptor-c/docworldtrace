# Repository Structure

This file is the working map for the current DocWorldTrace pilot repository.

## Top-Level Documents

| File | Role |
|---|---|
| `README.md` | Main project entrypoint |
| `01_background.md` - `09_pilot_verification.md` | Research plan and experiment design notes |
| `h1_h4_experiment_summary.md` | Main technical summary for H1-H5 pilot results |
| `h1_h5_presentation_report.md` | Presentation-oriented result report |
| `h1_h4_analysis_report.md` | Analysis, limitations, and action items |
| `h5_experiment_report.md` | Standalone H5 Qwen3-VL SFT report |
| `h5_closed_loop_trajectory_comparison.md` | H5 closed-loop answer-only vs trajectory examples |
| `references.md` | References |

## Code

| Path | Role |
|---|---|
| `docworldtrace/docenv.py` | Interactive document environment facade |
| `docworldtrace/loaders.py` | PDF loading/rendering/parsing |
| `docworldtrace/search.py` | Document search |
| `docworldtrace/verify.py` | Claim/evidence verification helpers |
| `docworldtrace/docverify.py` | DocVerify++ style trajectory checks |
| `docworldtrace/safe_eval.py` | Restricted numeric compute helper |
| `docworldtrace/pilot/` | H1-H5 experiment modules |

## Pilot Modules

| Module | Stage | Role |
|---|---|---|
| `docworldtrace/pilot/exp1_auto_runner.py` | H1 | Raw PDF suitability evaluation |
| `docworldtrace/pilot/generate_call_specs.py` | H1 | Deterministic call-spec generation |
| `docworldtrace/pilot/exp1_runner.py` | H1 | Tool-call execution/reporting |
| `docworldtrace/pilot/h2_rollout.py` | H2 | Teacher rollout execution |
| `docworldtrace/pilot/h2_eval.py` | H2 | Final answer evaluation |
| `docworldtrace/pilot/h3_docverify.py` | H3 | DocVerify++ positive filtering |
| `docworldtrace/pilot/h3_negative.py` | H3 | Negative/corrupted trajectory checks |
| `docworldtrace/pilot/h4_diversity.py` | H4 | Diversity analysis |
| `docworldtrace/pilot/h5_sft.py` | H5 | SFT dataset construction |
| `docworldtrace/pilot/h5_qwen_sft.py` | H5 | Qwen3-VL LoRA SFT |
| `docworldtrace/pilot/h5_qwen_eval.py` | H5 | Next-action adapter evaluation |
| `docworldtrace/pilot/h5_closed_loop.py` | H5 | Closed-loop DocEnv adapter evaluation |

## Scripts

| Script | Stage | Role |
|---|---|---|
| `scripts/run_h1_h4_pilot.sh` | H1-H4 | Main H1-H4 pilot entrypoint |
| `scripts/run_h2_h4_v5_pipeline.sh` | H2-H4 | Current v5 teacher/docverify/diversity pipeline |
| `scripts/run_prepared_h4_pipeline.sh` | H2-H4 | Server-side diverse-PDF prepared-seed pipeline |
| `scripts/build_diverse_pdf_seeds_v2.py` | H2 | Build checked diverse-PDF seeds |
| `scripts/build_diverse_pdf_seeds_v3_refuse_augmented.py` | H2/H5 | Build refuse-augmented next-round seeds |
| `scripts/run_h5_qwen3_vl_sft.sh` | H5 | Build SFT data, train adapters, run next-action eval |
| `scripts/run_h5_qwen3_vl_closed_loop.sh` | H5 | Run closed-loop adapter evaluation |
| `scripts/setup_h5_qwen_sft_env.sh` | H5 | Install Qwen3-VL SFT dependencies |
| `scripts/download_qwen3_vl_8b_modelscope.sh` | H5 | Download model into local `models/` |

Detailed script notes:

```text
scripts/README_h1_h4.md
scripts/README_h5_qwen3_vl.md
```

## Data Layout

| Path | Contents |
|---|---|
| `data/raw_pdfs/` | Local PDF corpus used by H1-H5 |
| `data/calls/` | H1 deterministic call specs |
| `data/reports/` | H1 reports and manual review figures |
| `data/h2/seeds/` | H2 seed JSONL and review files |
| `data/h2/rollouts_*` | H2 teacher rollout outputs |
| `data/h2/eval_*` | H2 answer/path evaluation summaries |
| `data/h3/docverify_plus_*` | H3 DocVerify++ outputs |
| `data/h3/negative_*` | H3 negative-control outputs |
| `data/h4/diversity_*` | H4 diversity outputs |
| `data/h5/sft_*` | H5 answer-only and trajectory SFT datasets |
| `data/h5/closed_loop_*` | H5 closed-loop evaluation outputs |

## Current Important Artifacts

| Artifact | Path |
|---|---|
| H1 manual review contact sheet | `data/reports/h1_manual_review/contact_sheet.png` |
| H2-H4 annotated example sheet | `data/reports/h2_h4_annotated_examples/h2_h4_annotated_examples.png` |
| H5 SFT data summary | `data/h5/sft_diverse_v2/summary.json` |
| H5 next-action eval summary | `runs/h5_qwen3_vl_diverse_v2/h5_qwen_eval_summary.json` |
| H5 closed-loop summary | `data/h5/closed_loop_diverse_v2/summary.json` |
| H5 closed-loop trajectory comparison | `h5_closed_loop_trajectory_comparison.md` |

## Local-Only Outputs

These should normally stay out of Git unless explicitly needed:

| Path | Reason |
|---|---|
| `models/` | Downloaded model weights |
| `runs/` | LoRA adapters/checkpoints and trainer state |
| `logs/` | Runtime logs |
| `.venv/` | Local virtual environment |
| `__pycache__/`, `.pytest_cache/` | Python/cache outputs |

## Recommended Review Before Commit

Run:

```bash
git status --short
```

Check whether new `data/` directories are intended to be committed. In general:

- Commit small seed/review/report files.
- Avoid committing model checkpoints, logs, and large temporary artifacts.
- Commit derived summaries only when they are part of the experiment evidence.

