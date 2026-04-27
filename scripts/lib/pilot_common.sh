#!/usr/bin/env bash

# Shared helpers for H1-H4 pilot scripts. This file is meant to be sourced.

pilot_root_dir() {
  local source_path="${BASH_SOURCE[0]}"
  cd "$(dirname "${source_path}")/../.." && pwd
}

pilot_activate_venv() {
  local root_dir="$1"
  local venv_dir="${VENV_DIR:-${root_dir}/.venv}"
  if [[ ! -d "${venv_dir}" ]]; then
    echo "Missing virtualenv: ${venv_dir}"
    echo "Run: bash ${root_dir}/scripts/setup_python_env.sh"
    exit 1
  fi
  # shellcheck disable=SC1091
  source "${venv_dir}/bin/activate"
}

pilot_require_file() {
  local path="$1"
  local label="${2:-file}"
  if [[ ! -f "${path}" ]]; then
    echo "Missing ${label}: ${path}"
    exit 1
  fi
}

pilot_require_dir() {
  local path="$1"
  local label="${2:-directory}"
  if [[ ! -d "${path}" ]]; then
    echo "Missing ${label}: ${path}"
    exit 1
  fi
}

pilot_load_env_file() {
  local env_file="$1"
  if [[ -f "${env_file}" ]]; then
    set -a
    # shellcheck disable=SC1090
    source "${env_file}"
    set +a
  fi
}
