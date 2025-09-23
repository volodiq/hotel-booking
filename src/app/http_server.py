from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI, HTTPException, Request, status

from app import models_registry  # noqa: F401
from app.container import container
from contexts.auth.api.http_router import router as auth_router
from contexts.users.api.http_router import router as users_router
from shared.core.errors import DomainError
from shared.providers.security import InvalidTokenData, SecurityException


async def domain_error_handler(request: Request, exc: DomainError):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=exc.details,
    )


async def security_error_handler(request: Request, exc: SecurityException):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=exc.details,
    )


async def invalid_token_error_handler(request: Request, exc: InvalidTokenData):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=exc.details,
    )


def create_app() -> FastAPI:
    app = FastAPI(
        title="Hotel booking API example",
        root_path="/api",
        exception_handlers={
            DomainError: domain_error_handler,
            SecurityException: security_error_handler,
            InvalidTokenData: invalid_token_error_handler,
        },
    )

    app.include_router(users_router)
    app.include_router(auth_router)
    setup_dishka(container=container, app=app)
    return app
