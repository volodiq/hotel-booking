from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
import uvicorn

from app import models_registry  # noqa: F401
from app.http_server.container import container
from app.http_server.controllers import setup_controllers
from app.http_server.docs import setup_docs
from app.http_server.errors_handlers import setup_exceptions_handlers


def create_app() -> FastAPI:
    app = FastAPI(root_path="/api")
    setup_controllers(app)
    setup_exceptions_handlers(app)
    setup_docs(app)
    setup_dishka(container=container, app=app)
    return app


if __name__ == "__main__":
    uvicorn.run(
        create_app,
        factory=True,
        host="0.0.0.0",
        port=8000,
    )
