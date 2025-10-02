from sqlalchemy import sql

from shared.infra.repositories import SARepository

from ..core import values, values1
from ..core.entities import User
from ..core.repositories import UserRepository
from .models import UserModel


class SAUserRepository(UserRepository, SARepository[UserModel]):
    model = UserModel

    @classmethod
    def to_entity(cls, model: UserModel) -> User:
        return User(
            oid=model.oid,
            first_name=values.FirstName(model.first_name),
            last_name=values.LastName(model.last_name),
            phone=values1.PhoneNumber(model.phone_number),
            created_at=model.created_at,
            password_hash=model.password_hash,
            is_superuser=model.is_superuser,
            is_hotel_admin=model.is_hotel_admin,
        )

    async def create_user(self, user: User):
        model = UserModel(
            oid=user.oid,
            first_name=user.first_name.value,
            last_name=user.last_name.value,
            phone_number=user.phone.value,
            created_at=user.created_at.replace(tzinfo=None),
            password_hash=user.password_hash,
            is_superuser=user.is_superuser,
            is_hotel_admin=user.is_hotel_admin,
        )
        self.create(model)

    async def get_user_by_oid(self, oid: str) -> User | None:
        model = await self.get_by_oid(oid)
        if not model:
            return None

        return self.to_entity(model)

    async def get_user_by_phone(self, phone: values1.PhoneNumber) -> User | None:
        stmt = sql.select(UserModel).where(UserModel.phone_number == phone.value)
        res = await self.session.scalars(stmt)
        user_db = res.one_or_none()
        if not user_db:
            return None

        return self.to_entity(user_db)

    async def update_user(self, user: User):
        stmt = (
            sql.update(UserModel)
            .where(UserModel.oid == user.oid)
            .values(
                first_name=user.first_name.value,
                last_name=user.last_name.value,
                phone_number=user.phone.value,
                created_at=user.created_at.replace(tzinfo=None),
                password_hash=user.password_hash,
                is_superuser=user.is_superuser,
                is_hotel_admin=user.is_hotel_admin,
            )
        )
        await self.session.execute(stmt)
