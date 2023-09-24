#!/usr/bin/env bash

set -euo pipefail

# Check if Pre-Commit is installed else stop project generation
if ! command -v pre-commit --version &>/dev/null; then
  exit 1
fi
