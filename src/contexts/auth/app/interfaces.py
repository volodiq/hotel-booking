from abc import ABC, abstractmethod

from .dtos import VerifyUserPasswordOut


class UsersGateway(ABC):
    @abstractmethod
    async def verify_user_password(
        self,
        raw_phone: str,
        raw_password: str,
    ) -> VerifyUserPasswordOut: ...
