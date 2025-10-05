DC := "docker compose --env-file .env"

app:
    @{{DC}} --profile app up --build

storage:
    @{{DC}} --profile storage up

cli args:
    @PYTHONPATH=./src uv run python src/bootstrap/cli.py {{args}}