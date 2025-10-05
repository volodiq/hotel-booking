DC=docker compose --env-file .env 


.PHONY: app
app:
	@$(DC) --profile app up --build


.PHONY: storage
storage:
	@$(DC) --profile storage up