from dataclasses import dataclass

from kernel.seedwork.entity import Entity

from . import values


@dataclass(eq=False, frozen=True)
class User(Entity):
    phone: values.PhoneNumber
    first_name: values.FirstName
    last_name: values.LastName
    password_hash: str
    is_superuser: bool = False
