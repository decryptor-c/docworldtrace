#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "${ROOT_DIR}"

bash "${ROOT_DIR}/scripts/install_system_deps.sh"
bash "${ROOT_DIR}/scripts/setup_python_env.sh"
bash "${ROOT_DIR}/scripts/check_server_env.sh"

echo
echo "Bootstrap complete."
echo "Next:"
echo "  1. source ${ROOT_DIR}/.venv/bin/activate"
echo "  2. bash ${ROOT_DIR}/scripts/run_pilot_exp1_sample.sh"
