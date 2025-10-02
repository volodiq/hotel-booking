#!/bin/sh

PYTHONPATH=./src uv run python src/app/cli/run.py "$@"
