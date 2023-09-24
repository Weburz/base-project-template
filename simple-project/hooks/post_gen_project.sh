#!/usr/bin/env bash

set -euo pipefail

# Initialise the generated project as a local Git repository
git init

# Generate the project files/folders and install the Pre-Commit hooks
pre-commit install --install-hooks
