#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"

SEED_FILE="${PREPARED_H2_SEED_FILE:-${ROOT_DIR}/data/h2/seeds/diverse_pdf_seeds_v1_checked.jsonl}"
TEACHER_CONFIG="${H2_TEACHER_CONFIG:-${ROOT_DIR}/data/h2/teachers.json}"
ROLLOUT_DIR="${PREPARED_H2_ROLLOUT_DIR:-${ROOT_DIR}/data/h2/rollouts_diverse_v1}"
EVAL_DIR="${PREPARED_H2_EVAL_DIR:-${ROOT_DIR}/data/h2/eval_diverse_v1}"
PATH_DIR="${PREPARED_H2_PATH_DIR:-${ROOT_DIR}/data/h2/eval_diverse_v1_path}"
DOCVERIFY_DIR="${PREPARED_H3_DOCVERIFY_DIR:-${ROOT_DIR}/data/h3/docverify_plus_diverse_v1}"
NEGATIVE_DIR="${PREPARED_H3_NEGATIVE_DIR:-${ROOT_DIR}/data/h3/negative_diverse_v1}"
DIVERSITY_DIR="${PREPARED_H4_DIVERSITY_DIR:-${ROOT_DIR}/data/h4/diversity_diverse_v1}"

RUN_H2="${RUN_H2:-1}"
RUN_H3="${RUN_H3:-1}"
RUN_H3_NEGATIVE="${RUN_H3_NEGATIVE:-1}"
RUN_H4="${RUN_H4:-1}"

pilot_require_file "${SEED_FILE}" "prepared H2 seed file"
pilot_require_dir "${ROOT_DIR}/data/raw_pdfs" "prepared PDF directory"
pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

echo "Prepared H4 pipeline"
echo "SEED_FILE=${SEED_FILE}"
echo "ROLLOUT_DIR=${ROLLOUT_DIR}"
echo "DIVERSITY_DIR=${DIVERSITY_DIR}"
echo "RUN_H2=${RUN_H2} RUN_H3=${RUN_H3} RUN_H3_NEGATIVE=${RUN_H3_NEGATIVE} RUN_H4=${RUN_H4}"

if [[ "${RUN_H2}" == "1" ]]; then
  echo
  echo "== H2 teacher rollouts from prepared seeds =="
  bash scripts/setup_h2_dmxapi_teachers.sh
  bash scripts/run_h2_rollouts.sh \
    "${SEED_FILE}" \
    "${TEACHER_CONFIG}" \
    "${ROLLOUT_DIR}"

  echo
  echo "== H2 eval and path review =="
  bash scripts/eval_h2_rollouts.sh "${ROLLOUT_DIR}" "${EVAL_DIR}"
  python scripts/review_h2_paths.py "${ROLLOUT_DIR}" "${PATH_DIR}"
fi

if [[ "${RUN_H3}" == "1" ]]; then
  echo
  echo "== H3 DocVerify++ =="
  bash scripts/run_h3_docverify_plus.sh "${ROLLOUT_DIR}" "${DOCVERIFY_DIR}"
fi

if [[ "${RUN_H3_NEGATIVE}" == "1" ]]; then
  echo
  echo "== H3 negative-control =="
  bash scripts/run_h3_negative.sh "${ROLLOUT_DIR}" "${NEGATIVE_DIR}"
fi

if [[ "${RUN_H4}" == "1" ]]; then
  echo
  echo "== H4 diversity =="
  bash scripts/run_h4_diversity.sh \
    "${ROLLOUT_DIR}" \
    "${DOCVERIFY_DIR}/docverify_review.json" \
    "${DIVERSITY_DIR}"
fi

echo
echo "Prepared H4 pipeline complete."
echo "Rollouts: ${ROLLOUT_DIR}"
echo "H3 DocVerify++: ${DOCVERIFY_DIR}"
echo "H4 diversity: ${DIVERSITY_DIR}"
