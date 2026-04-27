#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${ROOT_DIR}/data/h2/teachers.json"

mkdir -p "$(dirname "${TARGET}")"
cp "${ROOT_DIR}/pilot_h2/teachers.dmxapi.json" "${TARGET}"

echo "DMXAPI H2 teacher config written to ${TARGET}"
echo "Before rollout, set DMXAPI_API_KEY or run scripts/run_h2_dmxapi.sh with .env.dmxapi."
