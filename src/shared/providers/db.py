from typing import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from shared.providers.env import Env


class DBProvider(Provider):
    @provide(scope=Scope.APP)
    def db_session_pool(self, env: Env) -> async_sessionmaker:
        engine = create_async_engine(env.db_dsn)
        return async_sessionmaker(engine, expire_on_commit=False)

    @provide(scope=Scope.REQUEST)
    async def db_session(
        self,
        session_pool: async_sessionmaker,
    ) -> AsyncIterable[AsyncSession]:
        async with session_pool.begin() as session:
            yield session
