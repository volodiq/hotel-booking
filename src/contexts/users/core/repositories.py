from abc import ABC, abstractmethod

from . import values
from .entities import User


class UserRepository(ABC):
    @abstractmethod
    async def create_user(self, user: User): ...

    @abstractmethod
    async def get_user_by_oid(self, oid: str) -> User | None: ...

    @abstractmethod
    async def get_user_by_phone(self, phone: values.PhoneNumber) -> User | None: ...

    @abstractmethod
    async def update_user(self, user: User): ...
