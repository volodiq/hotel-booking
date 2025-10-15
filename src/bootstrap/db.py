from typing import AsyncIterable

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from . import config


db_engine = create_async_engine(config.db_dsn)
session_pool = async_sessionmaker(db_engine, expire_on_commit=False)


async def get_session() -> AsyncIterable[AsyncSession]:
    async with session_pool.begin() as session:
        yield session
