#!/bin/sh

PYTHONPATH=./src uv run python src/bootstrap/cli.py "$@"
