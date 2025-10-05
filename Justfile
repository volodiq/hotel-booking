DC := "docker compose --env-file .env"

app:
    @{{DC}} --profile app up --build

storage:
    @{{DC}} --profile storage up
