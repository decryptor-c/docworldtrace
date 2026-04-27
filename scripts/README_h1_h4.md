# H1-H4 Pilot Script Guide

This folder keeps the H1-H4 pilot entrypoints. The experiment outputs are under `data/`, while reusable Python implementations are under `docworldtrace/pilot/`.

## Recommended Entry Point

Run all H1-H4 stages:

```bash
bash scripts/run_h1_h4_pilot.sh
```

Run only selected stages:

```bash
RUN_H1=0 RUN_H2=0 RUN_H3=1 RUN_H3_NEGATIVE=1 RUN_H4=1 bash scripts/run_h1_h4_pilot.sh
```

Current default seed and output version is v5. Run the dedicated H2-H4 v5 pipeline with the refuse-diverse seed and the DMXAPI teacher set:

```bash
bash scripts/run_h2_h4_v5_pipeline.sh
```

## Stage Scripts

| Stage | Script | Main Output |
|---|---|---|
| H1 raw PDF suitability | `scripts/run_h1_rawdata_eval.sh` | `data/reports/rawdata_eval/` |
| H1 call specs | `scripts/generate_h1_call_specs.sh` | `data/calls/` |
| H1 tool execution | `scripts/run_h1_calls_batch.sh` | `data/reports/h1_calls/` |
| H2 rollouts | `scripts/run_h2_rollouts.sh` | `data/h2/rollouts_v5/` |
| H2 answer eval | `scripts/eval_h2_rollouts.sh` | `data/h2/eval_v5/` |
| H2 path review | `scripts/review_h2_paths.py` | `data/h2/eval_v5_path/` |
| H3 positive DocVerify++ | `scripts/run_h3_docverify_plus.sh` | `data/h3/docverify_plus_v5/` |
| H3 negative-control | `scripts/run_h3_negative.sh` | `data/h3/negative_v5/` |
| H4 diversity | `scripts/run_h4_diversity.sh` | `data/h4/diversity_v5/` |

## Current Teacher Set

`scripts/setup_h2_dmxapi_teachers.sh` writes `data/h2/teachers.json` with:

| Name | Model |
|---|---|
| `dmxapi_gpt4o_2024_11_20` | `gpt-4o-2024-11-20` |
| `dmxapi_gemini_2_5_flash` | `gemini-2.5-flash` |
| `dmxapi_gemini_3_1_flash_lite_preview` | `gemini-3.1-flash-lite-preview` |

## Python Modules

| Module | Responsibility |
|---|---|
| `docworldtrace/pilot/exp1_auto_runner.py` | H1 raw PDF suitability evaluation |
| `docworldtrace/pilot/generate_call_specs.py` | H1 deterministic tool-call spec generation |
| `docworldtrace/pilot/exp1_runner.py` | H1 tool-call execution and report generation |
| `docworldtrace/pilot/h2_rollout.py` | H2 teacher rollout execution |
| `docworldtrace/pilot/h2_eval.py` | H2 final-answer evaluation |
| `docworldtrace/pilot/h3_docverify.py` | H3 rule-based DocVerify++ positive filtering |
| `docworldtrace/pilot/h3_negative.py` | H3 corrupted trajectory generation and detection |
| `docworldtrace/pilot/h4_diversity.py` | H4 trajectory diversity analysis |

## Notes

- H2 uses teacher APIs. Make sure `.env.dmxapi` exists or export `DMXAPI_API_KEY`.
- H3 and H4 can be rerun from existing H2 rollouts without calling the teacher model.
- Current kept experiment data is v5. Older H2/H3/H4 versioned data was removed; see `data/cleanup_old_versions_deleted.md`.
- `scripts/lib/pilot_common.sh` contains shared shell helpers for root detection, virtualenv activation, and file/directory checks.
