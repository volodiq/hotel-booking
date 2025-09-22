from dataclasses import dataclass
import secrets

from shared.utils import calculate_password_hash

from ..core import values
from ..core.repositories import UserRepository
from . import internal_dto


@dataclass
class VerifyUserPasswordOut:
    is_valid: bool
    user_oid: str | None = None


@dataclass
class VerifyUserPassword:
    user_repository: UserRepository

    async def __call__(
        self,
        raw_phone: str,
        raw_password: str,
    ) -> internal_dto.VerifyUserPasswordOut:
        phone = values.PhoneNumber(raw_phone)

        user = await self.user_repository.get_user_by_phone(phone)
        if user is None:
            return internal_dto.VerifyUserPasswordOut(is_valid=False)

        password_hash = calculate_password_hash(raw_password)
        is_valid = secrets.compare_digest(user.password_hash, password_hash)
        if not is_valid:
            return internal_dto.VerifyUserPasswordOut(is_valid=False)

        return internal_dto.VerifyUserPasswordOut(is_valid=True, user_oid=user.oid)
