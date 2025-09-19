FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY uv.lock /app
COPY pyproject.toml /app
COPY .python-version /app

RUN uv sync --frozen --no-dev

COPY . /app