from sqlalchemy import sql

from shared.infra.repositories import SARepository

from ..core import values
from ..core.entities import User
from ..core.repositories import UserRepository
from .models import UserModel


class SAUserRepository(UserRepository, SARepository[UserModel]):
    model = UserModel

    async def create_user(self, user: User):
        model = UserModel(
            oid=user.oid,
            first_name=user.first_name.value,
            last_name=user.last_name.value,
            phone_number=user.phone.value,
            created_at=user.created_at.replace(tzinfo=None),
            password_hash=user.password_hash.value,
        )
        self.create(model)

    async def get_user_by_phone(self, phone: values.PhoneNumber) -> User | None:
        stmt = sql.select(UserModel).where(UserModel.phone_number == phone.value)
        res = await self.session.scalars(stmt)
        user_db = res.one_or_none()
        if not user_db:
            return None

        return User(
            oid=user_db.oid,
            first_name=values.FirstName(user_db.first_name),
            last_name=values.LastName(user_db.last_name),
            phone=values.PhoneNumber(user_db.phone_number),
            created_at=user_db.created_at,
            password_hash=user_db.password_hash,
        )
