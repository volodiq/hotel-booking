from fastapi import FastAPI

from contexts.auth.api.http_router import router as auth_router
from contexts.users.api.http_router import router as users_router


def setup_controllers(app: FastAPI) -> None:
    app.include_router(auth_router)
    app.include_router(users_router)
