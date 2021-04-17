#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort robtex_python/ tests/

black robtex_python/ tests/

mypy robtex_python/ tests/

pylint --fail-under 9 robtex_python/*.py

flake8 robtex_python/ tests/

bandit -r robtex_python/
