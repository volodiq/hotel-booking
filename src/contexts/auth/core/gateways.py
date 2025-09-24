from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class VerifyUserPasswordOut:
    is_valid: bool
    user_oid: str | None
    is_superuser: bool | None


class UsersGateway(ABC):
    @abstractmethod
    async def verify_user_password(
        self,
        raw_phone: str,
        raw_password: str,
    ) -> VerifyUserPasswordOut: ...
