from dataclasses import dataclass
from typing import AsyncIterable, Self

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from .env import Env


@dataclass
class SessionProvider:
    db_engine: AsyncEngine
    session_pool: async_sessionmaker

    async def get_session(self: Self) -> AsyncIterable[AsyncSession]:
        async with self.session_pool.begin() as session:
            yield session

    @classmethod
    def from_env(cls, env: Env) -> Self:
        db_engine = create_async_engine(env.db_dsn)
        session_pool = async_sessionmaker(db_engine, expire_on_commit=False)
        return cls(
            db_engine=db_engine,
            session_pool=session_pool,
        )
