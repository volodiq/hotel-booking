from dataclasses import dataclass

from contexts.users.domain import values
from shared.core.entity import Entity


@dataclass(eq=False, frozen=True)
class NewUser(Entity):
    phone: values.PhoneNumber
    first_name: values.FirstName
    last_name: values.LastName
