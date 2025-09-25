from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import uvicorn

from app import models_registry  # noqa: F401
from app.container import container
from app.http_server.handlers import exceptions_handlers
from app.http_server.router import router


def get_custom_openapi(app: FastAPI):
    schema = get_openapi(
        title="Hotel booking API example",
        version="1.0.0",
        routes=app.routes,
    )
    schema.setdefault("components", {}).setdefault("securitySchemes", {})["HTTPBearer"] = {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
    }

    return schema


def create_app() -> FastAPI:
    app = FastAPI(
        root_path="/api",
        exception_handlers=exceptions_handlers,
    )

    app.include_router(router)
    setup_dishka(container=container, app=app)

    app.openapi_schema = get_custom_openapi(app)
    return app


if __name__ == "__main__":
    uvicorn.run(
        create_app,
        factory=True,
        host="0.0.0.0",
        port=8000,
    )
