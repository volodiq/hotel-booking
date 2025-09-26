from abc import ABC, abstractmethod
from dataclasses import dataclass
import secrets

from shared.core.values import Password

from . import errors, values
from .entities import User
from .repositories import UserRepository


class PasswordHashService(ABC):
    @abstractmethod
    def calculate_password_hash(self, raw_password: str) -> str: ...


@dataclass
class CreateUserService:
    repository: UserRepository
    password_hash_service: PasswordHashService

    async def __call__(
        self,
        first_name: str,
        last_name: str,
        phone: str,
        password: str,
        is_superuser: bool = False,
    ):
        exists_user = await self.repository.get_user_by_phone(values.PhoneNumber(phone))
        if exists_user:
            raise errors.UserAlreadyExists()

        raw_password = Password(password)
        password_hash = self.password_hash_service.calculate_password_hash(raw_password.value)

        user = User(
            first_name=values.FirstName(first_name),
            last_name=values.LastName(last_name),
            phone=values.PhoneNumber(phone),
            password_hash=password_hash,
            is_superuser=is_superuser,
        )

        return await self.repository.create_user(user)


@dataclass
class GetUserByPhoneAndPasswordService:
    user_repository: UserRepository
    password_hash_service: PasswordHashService

    async def __call__(self, raw_phone: str, raw_password: str) -> User | None:
        phone = values.PhoneNumber(raw_phone)
        user = await self.user_repository.get_user_by_phone(phone)
        if user is None:
            return None

        password_hash = self.password_hash_service.calculate_password_hash(raw_password)
        is_valid = secrets.compare_digest(user.password_hash, password_hash)
        if not is_valid:
            return None

        return user
