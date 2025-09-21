from dataclasses import dataclass

from . import errors, values
from .entities import User
from .repositories import UserRepository


@dataclass
class CreateUserService:
    repository: UserRepository

    async def __call__(
        self,
        first_name: str,
        last_name: str,
        phone: str,
    ):
        exists_user = await self.repository.get_user_by_phone(values.PhoneNumber(phone))
        if exists_user:
            raise errors.UserAlreadyExists()

        user = User(
            first_name=values.FirstName(first_name),
            last_name=values.LastName(last_name),
            phone=values.PhoneNumber(phone),
        )
        return await self.repository.create_user(user)
