from dataclasses import dataclass

from ..core.services import GetUserByPhoneAndPasswordService


@dataclass
class VerifyUserPasswordOut:
    is_valid: bool
    user_oid: str | None = None
    is_superuser: bool | None = None
    is_hotel_admin: bool | None = None


@dataclass
class VerifyUserPassword:
    verify_user_password_service: GetUserByPhoneAndPasswordService

    async def __call__(
        self,
        raw_phone: str,
        raw_password: str,
    ) -> VerifyUserPasswordOut:
        user = await self.verify_user_password_service(raw_phone, raw_password)
        if user is None:
            return VerifyUserPasswordOut(is_valid=False)

        return VerifyUserPasswordOut(
            is_valid=True,
            user_oid=user.oid,
            is_superuser=user.is_superuser,
            is_hotel_admin=user.is_hotel_admin,
        )
