from dishka.integrations.fastapi import FastapiProvider, setup_dishka
from fastapi import FastAPI
import uvicorn

from app import models_registry  # noqa: F401
from app.container import make_container
from app.http_server.controllers import setup_controllers
from app.http_server.error_handlers import setup_exceptions_handlers


def create_app() -> FastAPI:
    app = FastAPI(root_path="/api")
    setup_controllers(app)
    setup_exceptions_handlers(app)
    setup_dishka(
        container=make_container(FastapiProvider()),
        app=app,
    )
    return app


if __name__ == "__main__":
    uvicorn.run(
        create_app,
        factory=True,
        host="0.0.0.0",
        port=8000,
    )
