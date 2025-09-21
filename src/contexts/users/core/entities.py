from dataclasses import dataclass

from shared.core.entity import Entity

from . import values


@dataclass(eq=False, frozen=True)
class User(Entity):
    phone: values.PhoneNumber
    first_name: values.FirstName
    last_name: values.LastName
    password_hash: values.PasswordHash
