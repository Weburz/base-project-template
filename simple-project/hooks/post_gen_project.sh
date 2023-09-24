#!/usr/bin/env bash

set -euo pipefail

# Generate the project files/folders and install the Pre-Commit hooks
pre-commit install --install-hooks
