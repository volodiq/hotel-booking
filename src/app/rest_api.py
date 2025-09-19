from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app import all_models  # noqa: F401
from app.container import container
from contexts.users.rest_api.router import router as users_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Hotel booking API example",
        root_path="/api",
    )
    app.include_router(users_router)
    setup_dishka(container=container, app=app)
    return app
