from abc import ABC, abstractmethod

from .entities import User


class UserRepository(ABC):
    @abstractmethod
    async def create_user(self, user: User): ...

    @abstractmethod
    async def get_user_by_phone(self, phone: str) -> User | None: ...
