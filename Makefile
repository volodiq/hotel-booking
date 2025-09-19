DC=docker compose
APP_NAME=hotel-booking-backend

# App
APP-DC=$(DC) -f ./docker/app.compose.yaml -p $(APP_NAME) --env-file .env

.PHONY: app
app:
	@$(APP-DC) down
	@$(APP-DC) up --build

# Storage
STORAGE-DC=$(DC) -f ./docker/storage.compose.yaml -p $(APP_NAME) --env-file .env

.PHONY: storage
storage:
	@$(STORAGE-DC) down
	@$(STORAGE-DC) up