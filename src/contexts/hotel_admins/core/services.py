from abc import ABC, abstractmethod
from dataclasses import dataclass

from kernel.security.dtos import Principal

from . import entities, errors, repositories, values


class PasswordHashService(ABC):
    @abstractmethod
    def calculate_password_hash(self, raw_password: str) -> str: ...


@dataclass
class CreateHotelAdminService:
    hotel_admin_repository: repositories.HotelAdminRepository
    password_hash_service: PasswordHashService
    principal: Principal

    async def __call__(
        self,
        first_name: str,
        last_name: str,
        middle_name: str,
        phone: str,
        raw_password: str,
        email: str,
    ):
        if "superuser" not in self.principal.roles:
            raise errors.HotelAdminCreateForbidden()

        exists_hotel_admin = await self.hotel_admin_repository.get_hotel_admin_by_phone(phone)
        if exists_hotel_admin is not None:
            raise errors.HotelAdminAlreadyExists()

        password = values.Password(raw_password)
        password_hash = self.password_hash_service.calculate_password_hash(password.value)

        hotel_admin = entities.HotelAdmin(
            first_name=values.FirstName(first_name),
            last_name=values.LastName(last_name),
            middle_name=values.MiddleName(middle_name),
            phone=values.PhoneNumber(phone),
            email=values.Email(email),
            password_hash=password_hash,
        )

        return await self.hotel_admin_repository.create_hotel_admin(hotel_admin)
