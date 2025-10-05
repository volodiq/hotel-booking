from typing import AsyncIterable

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from .env import Env


def _get_session_pool(db_dsn: str) -> async_sessionmaker:
    engine = create_async_engine(db_dsn)
    return async_sessionmaker(engine, expire_on_commit=False)


async def get_sa_session_pool(env: Env) -> async_sessionmaker:
    return _get_session_pool(env.db_dsn)


async def get_sa_session(session_pool: async_sessionmaker) -> AsyncIterable[AsyncSession]:
    async with session_pool.begin() as session:
        yield session
