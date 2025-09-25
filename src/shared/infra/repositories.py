from typing import Generic, TypeVar

from sqlalchemy import sql
from sqlalchemy.ext.asyncio import AsyncSession

from .models import DBModel


MT = TypeVar("MT", bound=DBModel)


class SARepository(Generic[MT]):
    model: type[MT]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_oid(self, oid: str) -> MT | None:
        stmt = sql.select(self.model).where(self.model.oid == oid)
        res = await self.session.scalars(stmt)
        return res.one_or_none()

    def create(self, model: MT) -> None:
        self.session.add(model)
