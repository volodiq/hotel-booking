from abc import ABC, abstractmethod
from dataclasses import dataclass

from sqlalchemy import sql
from sqlalchemy.ext.asyncio import AsyncSession

from .db_models import UserModel
from .domain.entities import NewUser


# TODO: Вынести базовый репозиторий SQLAlchemy в core


@dataclass
class UserRepository(ABC):
    @abstractmethod
    async def create_user(self, user: NewUser): ...

    @abstractmethod
    async def get_user_by_phone(self, phone: str) -> UserModel | None: ...


@dataclass
class SAUserRepository(UserRepository):
    session: AsyncSession

    async def create_user(self, user: NewUser):
        model = UserModel(
            oid=user.oid,
            first_name=user.first_name.value,
            last_name=user.last_name.value,
            phone_number=user.phone.value,
            created_at=user.created_at.replace(tzinfo=None),
        )
        self.session.add(model)

    async def get_user_by_phone(self, phone: str) -> UserModel | None:
        stmt = sql.select(UserModel).where(UserModel.phone_number == phone)
        res = await self.session.scalars(stmt)
        return res.one_or_none()
