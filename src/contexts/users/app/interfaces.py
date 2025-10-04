from abc import ABC, abstractmethod

from ..core import entities, values


class UserRepository(ABC):
    @abstractmethod
    async def get_user_by_oid(self, oid: str) -> entities.User | None: ...

    @abstractmethod
    async def get_user_by_phone(self, phone: values.PhoneNumber) -> entities.User | None: ...

    @abstractmethod
    async def save(self, user: entities.User): ...
