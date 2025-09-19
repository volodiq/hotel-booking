from typing import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from providers.env import Env


class DBSessionPoolProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_db_session_pool(self, env: Env) -> async_sessionmaker:
        engine = create_async_engine(env.db_dsn)
        return async_sessionmaker(engine, expire_on_commit=False)


class DBSessionProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def provide_db_session(
        self,
        session_pool: async_sessionmaker,
    ) -> AsyncIterable[AsyncSession]:
        async with session_pool.begin() as session:
            yield session
