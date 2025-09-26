from dataclasses import dataclass, replace
from typing import Self

from system.seedwork.entity import Entity

from . import errors, values


@dataclass(eq=False, frozen=True)
class User(Entity):
    phone: values.PhoneNumber
    first_name: values.FirstName
    last_name: values.LastName
    password_hash: str
    is_superuser: bool = False
    is_hotel_admin: bool = False

    def make_hotel_admin(self) -> Self:
        if self.is_hotel_admin:
            raise errors.UserAlreadyHotelAdmin()
        return replace(self, is_hotel_admin=True)
