Cleanup timestamp: 2026-04-27T20:05:34

Deleted paths:
- data/h2/rollouts
- data/h2/rollouts_v2
- data/h2/rollouts_v2_fixed
- data/h2/rollouts_v2_retry
- data/h2/rollouts_v3
- data/h2/rollouts_v4
- data/h2/baseline_no_tool_v3
- data/h2/eval
- data/h2/eval_v2_fixed
- data/h2/eval_v2_retry
- data/h2/eval_v2_retry_adjusted
- data/h2/eval_v2_retry_path_script
- data/h2/eval_v3
- data/h2/eval_v3_path
- data/h2/eval_v4
- data/h2/eval_v4_path
- data/h2/eval_no_tool_v3
- data/h3/docverify_plus_v4
- data/h3/negative_v4
- data/h4/diversity_v4
- data/h2/seeds/pilot_seeds.jsonl
- data/h2/seeds/pilot_seeds.summary.json
- data/h2/seeds/pilot_seeds_v2.jsonl
- data/h2/seeds/pilot_seeds_v2.summary.json
- data/h2/seeds/pilot_seeds_v2_agent_check.md
- data/h2/seeds/pilot_seeds_v2_review.jsonl
- data/h2/seeds/pilot_seeds_v2_review.review.md
- data/h2/seeds/pilot_seeds_v2_review.summary.json
- data/h2/seeds/pilot_seeds_v2_review_decisions.md
- data/h2/seeds/pilot_seeds_v3.jsonl
- data/h2/seeds/pilot_seeds_v3.review.md
- data/h2/seeds/pilot_seeds_v3.summary.json
- data/h2/seeds/pilot_seeds_v4.jsonl
- data/h2/seeds/pilot_seeds_v4.review.md
- data/h2/seeds/pilot_seeds_v4.summary.json

Kept current paths:
- data/h2/seeds/pilot_seeds_v5.jsonl
- data/h2/seeds/pilot_seeds_v5.review.md
- data/h2/seeds/huggingface/
- data/h2/rollouts_v5/
- data/h2/eval_v5/
- data/h2/eval_v5_path/
- data/h3/docverify_plus_v5/
- data/h3/negative_v5/
- data/h4/diversity_v5/
- data/reports/
- data/raw_pdfs/

Additional cleanup:
- data/h2/h2_v3_control_comparison.md
- scripts/__pycache__/

Deleted old scripts:
- scripts/build_h2_v3_seeds.py
- scripts/build_h2_v4_seeds.py
- scripts/compare_h2_v3_control.sh
- scripts/generate_h2_seed_review.sh
- scripts/generate_h2_seeds.sh
- scripts/make_h2_v5_refuse_diverse.py
- scripts/run_h2_dmxapi.sh
- scripts/run_h2_no_tool_baseline.sh
- scripts/run_h2_v4_pipeline.sh
- scripts/run_h3_exp3_lite.sh
- scripts/sync_h2_rollout_seed_paths.py

Updated remaining scripts to v5 defaults:
- scripts/run_h2_rollouts.sh
- scripts/run_h3_negative.sh
- scripts/rerun_h2_failed.sh
- scripts/run_h5_pilot.sh

Deleted old H5 data:
- data/h5/eval_v4/
- data/h5/sft_v4/
