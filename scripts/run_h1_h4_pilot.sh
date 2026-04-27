#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"

RUN_H1="${RUN_H1:-1}"
RUN_H2="${RUN_H2:-1}"
RUN_H3="${RUN_H3:-1}"
RUN_H3_NEGATIVE="${RUN_H3_NEGATIVE:-1}"
RUN_H4="${RUN_H4:-1}"

PDF_DIR="${PDF_DIR:-${ROOT_DIR}/data/raw_pdfs}"
H1_CALL_DIR="${H1_CALL_DIR:-${ROOT_DIR}/data/calls}"
H1_REPORT_DIR="${H1_REPORT_DIR:-${ROOT_DIR}/data/reports/h1_calls}"
H1_RAWDATA_REPORT_DIR="${H1_RAWDATA_REPORT_DIR:-${ROOT_DIR}/data/reports/rawdata_eval}"

H2_SEED_FILE="${H2_SEED_FILE:-${ROOT_DIR}/data/h2/seeds/pilot_seeds_v5.jsonl}"
H2_TEACHER_CONFIG="${H2_TEACHER_CONFIG:-${ROOT_DIR}/data/h2/teachers.json}"
H2_ROLLOUT_DIR="${H2_ROLLOUT_DIR:-${ROOT_DIR}/data/h2/rollouts_v5}"
H2_EVAL_DIR="${H2_EVAL_DIR:-${ROOT_DIR}/data/h2/eval_v5}"
H2_PATH_DIR="${H2_PATH_DIR:-${ROOT_DIR}/data/h2/eval_v5_path}"
H2_REPEATS="${H2_REPEATS:-2}"

H3_OUT_DIR="${H3_OUT_DIR:-${ROOT_DIR}/data/h3/docverify_plus_v5}"
H3_NEGATIVE_OUT_DIR="${H3_NEGATIVE_OUT_DIR:-${ROOT_DIR}/data/h3/negative_v5}"
H4_OUT_DIR="${H4_OUT_DIR:-${ROOT_DIR}/data/h4/diversity_v5}"

cd "${ROOT_DIR}"

echo "H1-H4 pilot pipeline"
echo "ROOT_DIR=${ROOT_DIR}"
echo "RUN_H1=${RUN_H1} RUN_H2=${RUN_H2} RUN_H3=${RUN_H3} RUN_H3_NEGATIVE=${RUN_H3_NEGATIVE} RUN_H4=${RUN_H4}"

if [[ "${RUN_H1}" == "1" ]]; then
  echo
  echo "== H1: rawdata eval, call spec generation, and tool-call batch =="
  bash scripts/run_h1_rawdata_eval.sh "${PDF_DIR}" "${H1_RAWDATA_REPORT_DIR}"
  bash scripts/generate_h1_call_specs.sh "${PDF_DIR}" "${H1_CALL_DIR}"
  bash scripts/run_h1_calls_batch.sh "${PDF_DIR}" "${H1_CALL_DIR}" "${H1_REPORT_DIR}"
fi

if [[ "${RUN_H2}" == "1" ]]; then
  echo
  echo "== H2: teacher rollouts, answer eval, and path review =="
  bash scripts/setup_h2_dmxapi_teachers.sh
  H2_REPEATS="${H2_REPEATS}" bash scripts/run_h2_rollouts.sh \
    "${H2_SEED_FILE}" \
    "${H2_TEACHER_CONFIG}" \
    "${H2_ROLLOUT_DIR}"
  bash scripts/eval_h2_rollouts.sh "${H2_ROLLOUT_DIR}" "${H2_EVAL_DIR}"
  python scripts/review_h2_paths.py "${H2_ROLLOUT_DIR}" "${H2_PATH_DIR}"
fi

if [[ "${RUN_H3}" == "1" ]]; then
  echo
  echo "== H3: DocVerify++ positive trajectory filtering =="
  bash scripts/run_h3_docverify_plus.sh "${H2_ROLLOUT_DIR}" "${H3_OUT_DIR}"
fi

if [[ "${RUN_H3_NEGATIVE}" == "1" ]]; then
  echo
  echo "== H3 negative-control: corrupted trajectory detection =="
  bash scripts/run_h3_negative.sh "${H2_ROLLOUT_DIR}" "${H3_NEGATIVE_OUT_DIR}"
fi

if [[ "${RUN_H4}" == "1" ]]; then
  echo
  echo "== H4: trajectory diversity =="
  bash scripts/run_h4_diversity.sh \
    "${H2_ROLLOUT_DIR}" \
    "${H3_OUT_DIR}/docverify_review.json" \
    "${H4_OUT_DIR}"
fi

echo
echo "H1-H4 pipeline complete."
echo "H1 reports: ${H1_REPORT_DIR}"
echo "H2 rollouts: ${H2_ROLLOUT_DIR}"
echo "H2 eval: ${H2_EVAL_DIR}"
echo "H2 path review: ${H2_PATH_DIR}"
echo "H3 DocVerify++: ${H3_OUT_DIR}"
echo "H3 negative-control: ${H3_NEGATIVE_OUT_DIR}"
echo "H4 diversity: ${H4_OUT_DIR}"
