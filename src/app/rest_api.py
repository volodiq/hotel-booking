from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI, HTTPException, Request, status

from app import all_models  # noqa: F401
from app.container import container
from contexts.users.api.router import router as users_router
from shared.core.exceptions import DomainError


async def domain_error_handler(request: Request, exc: DomainError):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=exc.details,
    )


def create_app() -> FastAPI:
    app = FastAPI(
        title="Hotel booking API example",
        root_path="/api",
        exception_handlers={
            DomainError: domain_error_handler,
        },
    )

    app.include_router(users_router)
    setup_dishka(container=container, app=app)
    return app
