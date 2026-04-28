#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"
DOCVERIFY_JSON="${1:-${ROOT_DIR}/data/h3/docverify_plus_v5/docverify_review.json}"
OUT_DIR="${2:-${ROOT_DIR}/data/h3/natural_gt_v5}"
SAMPLE_SIZE="${H3_NATURAL_GT_SAMPLE_SIZE:-100}"

pilot_require_file "${DOCVERIFY_JSON}" "DocVerify++ review JSON"

pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

python -m docworldtrace.pilot.h3_natural_gt \
  --docverify "${DOCVERIFY_JSON}" \
  --out-dir "${OUT_DIR}" \
  --sample-size "${SAMPLE_SIZE}"

echo
echo "H3 natural-distribution manual GT sample written to ${OUT_DIR}"
