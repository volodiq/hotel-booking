from dataclasses import dataclass
import secrets

from ..core import values
from ..core.repositories import UserRepository
from ..core.services import PasswordHashService


@dataclass
class VerifyUserPasswordOut:
    is_valid: bool
    user_oid: str | None = None
    is_superuser: bool | None = None


@dataclass
class VerifyUserPassword:
    user_repository: UserRepository
    password_hash_service: PasswordHashService

    async def __call__(
        self,
        raw_phone: str,
        raw_password: str,
    ) -> VerifyUserPasswordOut:
        phone = values.PhoneNumber(raw_phone)

        user = await self.user_repository.get_user_by_phone(phone)
        if user is None:
            return VerifyUserPasswordOut(is_valid=False)

        password_hash = self.password_hash_service.calculate_password_hash(raw_password)
        is_valid = secrets.compare_digest(user.password_hash, password_hash)
        if not is_valid:
            return VerifyUserPasswordOut(is_valid=False)

        return VerifyUserPasswordOut(
            is_valid=True,
            user_oid=user.oid,
            is_superuser=user.is_superuser,
        )
