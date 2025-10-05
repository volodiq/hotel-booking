from dataclasses import dataclass

from sqlalchemy import sql
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from ..app import entities, values
from ..app.interfaces import UserRepository
from .models import UserModel


@dataclass
class SAUserRepository(UserRepository):
    session: AsyncSession

    @staticmethod
    def to_entity(model: UserModel) -> entities.User:
        return entities.User(
            oid=model.oid,
            first_name=values.FirstName(model.first_name),
            last_name=values.LastName(model.last_name),
            phone=values.PhoneNumber(model.phone_number),
            created_at=model.created_at,
            password_hash=model.password_hash,
            is_superuser=model.is_superuser,
            is_hotel_admin=model.is_hotel_admin,
        )

    @staticmethod
    def to_model(user: entities.User) -> UserModel:
        return UserModel(
            oid=user.oid,
            first_name=user.first_name.value,
            last_name=user.last_name.value,
            phone_number=user.phone.value,
            created_at=user.created_at.replace(tzinfo=None),
            password_hash=user.password_hash,
            is_superuser=user.is_superuser,
            is_hotel_admin=user.is_hotel_admin,
        )

    async def save(self, user: entities.User) -> None:
        model = self.to_model(user)
        insert_stmt = insert(UserModel).values(
            oid=model.oid,
            first_name=model.first_name,
            last_name=model.last_name,
            phone_number=model.phone_number,
            created_at=model.created_at,
            password_hash=model.password_hash,
            is_superuser=model.is_superuser,
            is_hotel_admin=model.is_hotel_admin,
        )
        upsert_stmt = insert_stmt.on_conflict_do_update(
            index_elements=[UserModel.oid],
            set_={
                "first_name": insert_stmt.excluded.first_name,
                "last_name": insert_stmt.excluded.last_name,
                "phone_number": insert_stmt.excluded.phone_number,
                "password_hash": insert_stmt.excluded.password_hash,
                "is_superuser": insert_stmt.excluded.is_superuser,
                "is_hotel_admin": insert_stmt.excluded.is_hotel_admin,
            },
        )
        await self.session.execute(upsert_stmt)

    async def get_user_by_oid(self, oid: str) -> entities.User | None:
        stmt = sql.select(UserModel).where(UserModel.oid == oid)
        res = await self.session.scalars(stmt)
        model = res.one_or_none()
        if not model:
            return None

        return self.to_entity(model)

    async def get_user_by_phone(self, phone: values.PhoneNumber) -> entities.User | None:
        stmt = sql.select(UserModel).where(UserModel.phone_number == phone.value)
        res = await self.session.scalars(stmt)
        user_db = res.one_or_none()
        if not user_db:
            return None

        return self.to_entity(user_db)
