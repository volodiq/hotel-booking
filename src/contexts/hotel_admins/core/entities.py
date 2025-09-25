from dataclasses import dataclass
from typing import Self

from kernel.seedwork.entity import Entity

from . import errors, values


@dataclass(frozen=True, eq=True)
class HotelAdmin(Entity):
    """
    Администратор отеля/отелей
    Добавляется root-администратором, по договоренности.
    """

    first_name: values.FirstName
    last_name: values.LastName
    middle_name: values.MiddleName
    phone: values.PhoneNumber
    email: values.Email
    password_hash: str
    is_banned: bool = False

    def ban(self) -> Self:
        if self.is_banned:
            raise errors.HotelAdminAlreadyBanned()

        return self.__class__(
            first_name=self.first_name,
            last_name=self.last_name,
            middle_name=self.middle_name,
            phone=self.phone,
            email=self.email,
            password_hash=self.password_hash,
            is_banned=True,
        )
