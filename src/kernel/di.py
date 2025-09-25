from datetime import timedelta
from typing import AsyncIterable

from dishka import Provider, Scope
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from .db_session import get_session_pool
from .env import Env, get_env
from .security.services import PyJWTTokenService, TokenService


def get_token_service(env: Env) -> TokenService:
    return PyJWTTokenService(
        secret_key=env.SECRET_KEY,
        access_token_ttl=timedelta(hours=1),
        refresh_token_ttl=timedelta(weeks=1),
    )


async def get_db_session(session_pool: async_sessionmaker) -> AsyncIterable[AsyncSession]:
    async with session_pool.begin() as session:
        yield session


kernel_provider = Provider()
kernel_provider.provide(get_env, scope=Scope.APP)
kernel_provider.provide(get_session_pool, scope=Scope.APP)
kernel_provider.provide(get_token_service, scope=Scope.APP)
kernel_provider.provide(get_db_session, scope=Scope.REQUEST)
