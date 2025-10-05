from functools import partial
from http import HTTPStatus
from typing import NoReturn

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI, HTTPException, Request
import uvicorn

from bootstrap import models_registry  # noqa: F401
from bootstrap.container import provider
from contexts.auth.api.http_router import router as auth_router
from contexts.users.api.http_router import router as users_router
from shared.app.errors import ApplicationError, SecurityException


def setup_controllers(app: FastAPI) -> None:
    app.include_router(auth_router)
    app.include_router(users_router)


def setup_exceptions_handlers(app: FastAPI) -> None:
    app.add_exception_handler(ApplicationError, partial(error_handler, HTTPStatus.BAD_REQUEST))
    app.add_exception_handler(SecurityException, partial(error_handler, HTTPStatus.UNAUTHORIZED))


async def error_handler(
    status_code: HTTPStatus,
    request: Request,
    exc: ApplicationError | SecurityException,
) -> NoReturn:
    raise HTTPException(
        status_code=status_code,
        detail=exc.details,
    )


def create_app() -> FastAPI:
    app = FastAPI(root_path="/api")
    setup_controllers(app)
    setup_exceptions_handlers(app)
    setup_dishka(
        container=make_async_container(provider),
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
