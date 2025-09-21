from dataclasses import dataclass

from ..infra.repositories import UserRepository
from . import exceptions as exc, values
from .entities import NewUser


@dataclass
class CreateUserService:
    repository: UserRepository

    async def __call__(
        self,
        first_name: str,
        last_name: str,
        phone: str,
    ):
        exists_user = await self.repository.get_user_by_phone(phone)
        if exists_user:
            raise exc.UserAlreadyExists()

        user = NewUser(
            first_name=values.FirstName(first_name),
            last_name=values.LastName(last_name),
            phone=values.PhoneNumber(phone),
        )
        return await self.repository.create_user(user)
