#!/bin/sh

PYTHONPATH=./src uv run python -m src.app.cli "$@"
