#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"

SEED_FILE="${H2_V5_SEED_FILE:-${ROOT_DIR}/data/h2/seeds/pilot_seeds_v5.jsonl}"
TEACHER_CONFIG="${H2_TEACHER_CONFIG:-${ROOT_DIR}/data/h2/teachers.json}"
ROLLOUT_DIR="${H2_V5_ROLLOUT_DIR:-${ROOT_DIR}/data/h2/rollouts_v5}"
EVAL_DIR="${H2_V5_EVAL_DIR:-${ROOT_DIR}/data/h2/eval_v5}"
PATH_DIR="${H2_V5_PATH_DIR:-${ROOT_DIR}/data/h2/eval_v5_path}"
DOCVERIFY_DIR="${H3_V5_DOCVERIFY_DIR:-${ROOT_DIR}/data/h3/docverify_plus_v5}"
NEGATIVE_DIR="${H3_V5_NEGATIVE_DIR:-${ROOT_DIR}/data/h3/negative_v5}"
DIVERSITY_DIR="${H4_V5_DIVERSITY_DIR:-${ROOT_DIR}/data/h4/diversity_v5}"
REPEATS="${H2_REPEATS:-2}"

pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

pilot_require_file "${SEED_FILE}" "H2 v5 seed file"

bash scripts/setup_h2_dmxapi_teachers.sh

H2_REPEATS="${REPEATS}" bash scripts/run_h2_rollouts.sh \
  "${SEED_FILE}" \
  "${TEACHER_CONFIG}" \
  "${ROLLOUT_DIR}"

bash scripts/eval_h2_rollouts.sh \
  "${ROLLOUT_DIR}" \
  "${EVAL_DIR}"

python scripts/review_h2_paths.py \
  "${ROLLOUT_DIR}" \
  "${PATH_DIR}"

bash scripts/run_h3_docverify_plus.sh \
  "${ROLLOUT_DIR}" \
  "${DOCVERIFY_DIR}"

bash scripts/run_h3_negative.sh \
  "${ROLLOUT_DIR}" \
  "${NEGATIVE_DIR}"

bash scripts/run_h4_diversity.sh \
  "${ROLLOUT_DIR}" \
  "${DOCVERIFY_DIR}/docverify_review.json" \
  "${DIVERSITY_DIR}"

echo
echo "H2-H4 v5 pipeline complete."
echo "Seeds: ${SEED_FILE}"
echo "Teachers: ${TEACHER_CONFIG}"
echo "Rollouts: ${ROLLOUT_DIR}"
echo "H2 eval: ${EVAL_DIR}"
echo "H2 path review: ${PATH_DIR}"
echo "H3 DocVerify++: ${DOCVERIFY_DIR}"
echo "H3 negative-control: ${NEGATIVE_DIR}"
echo "H4 diversity: ${DIVERSITY_DIR}"
