#!/bin/sh

PYTHONPATH=./src uv run uvicorn \
    --factory src.app.rest_api:create_app \
    --host 0.0.0.0 --port 8000