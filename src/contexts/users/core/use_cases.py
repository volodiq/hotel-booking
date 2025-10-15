from dataclasses import dataclass

from shared.core.dtos import Principal
from shared.core.interfaces import PasswordService

from . import entities, errors, values
from .interfaces import UserRepository


@dataclass
class CreateUser:
    repository: UserRepository
    password_service: PasswordService

    async def __call__(
        self,
        first_name: str,
        last_name: str,
        phone: str,
        password: str,
        is_superuser: bool = False,
        is_hotel_admin: bool = False,
    ):
        exists_user = await self.repository.get_user_by_phone(values.PhoneNumber(phone))
        if exists_user:
            raise errors.UserAlreadyExists()

        raw_password = values.Password(password)
        password_hash = self.password_service.calculate_password_hash(raw_password.value)

        user = entities.User(
            first_name=values.FirstName(first_name),
            last_name=values.LastName(last_name),
            phone=values.PhoneNumber(phone),
            password_hash=password_hash,
            is_superuser=is_superuser,
            is_hotel_admin=is_hotel_admin,
        )

        return await self.repository.save(user)


@dataclass
class GetUserByPhoneAndPassword:
    user_repository: UserRepository
    password_service: PasswordService

    async def __call__(self, raw_phone: str, raw_password: str) -> entities.User | None:
        phone = values.PhoneNumber(raw_phone)
        user = await self.user_repository.get_user_by_phone(phone)
        if user is None:
            return None

        is_valid = self.password_service.check_password(
            raw_password=raw_password,
            password_hash=user.password_hash,
        )
        if not is_valid:
            return None

        return user


@dataclass
class MakeHotelAdmin:
    user_repository: UserRepository

    async def __call__(self, principal: Principal, user_oid: str):
        if "superuser" not in principal.roles:
            raise errors.MakeHotelAdminForbidden()

        user = await self.user_repository.get_user_by_oid(user_oid)
        if user is None:
            raise errors.UserNotFound()

        user = user.make_hotel_admin()
        return await self.user_repository.save(user)
