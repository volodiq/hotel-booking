from datetime import timedelta
from os import getenv
from typing import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from .db_session import get_session_pool
from .env import Env
from .security.services import PyJWTTokenService, TokenService


class KernelProvider(Provider):
    @provide(scope=Scope.APP)
    def env(self) -> Env:
        app_run_as_service = getenv("APP_RUN_AS_SERVICE")
        if app_run_as_service:
            return Env()  # type: ignore
        return Env(DBMS_HOST="localhost")  # type: ignore

    @provide(scope=Scope.APP)
    def token_service(self, env: Env) -> TokenService:
        return PyJWTTokenService(
            secret_key=env.SECRET_KEY,
            access_token_ttl=timedelta(hours=1),
            refresh_token_ttl=timedelta(weeks=1),
        )

    @provide(scope=Scope.APP)
    def db_session_pool(self, env: Env) -> async_sessionmaker:
        return get_session_pool(env)

    @provide(scope=Scope.REQUEST)
    async def db_session(
        self,
        session_pool: async_sessionmaker,
    ) -> AsyncIterable[AsyncSession]:
        async with session_pool.begin() as session:
            yield session
