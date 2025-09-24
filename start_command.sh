#!/bin/sh

PYTHONPATH=./src uv run python src/app/cli.py "$@"
