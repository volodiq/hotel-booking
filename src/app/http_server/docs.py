from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def get_custom_openapi(app: FastAPI) -> dict:
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


def setup_docs(app: FastAPI) -> None:
    app.openapi_schema = get_custom_openapi(app)
