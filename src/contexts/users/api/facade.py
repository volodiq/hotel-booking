from dataclasses import dataclass

from ..core import use_cases


@dataclass
class VerifyUserPasswordOut:
    is_valid: bool
    user_oid: str | None = None
    is_superuser: bool | None = None
    is_hotel_admin: bool | None = None


@dataclass
class UsersFacade:
    _get_user_by_phone_password: use_cases.GetUserByPhoneAndPassword

    async def verify_user_password(
        self,
        raw_phone: str,
        raw_password: str,
    ) -> VerifyUserPasswordOut:
        user = await self._get_user_by_phone_password(raw_phone, raw_password)
        if user is None:
            return VerifyUserPasswordOut(is_valid=False)

        return VerifyUserPasswordOut(
            is_valid=True,
            user_oid=user.oid,
            is_superuser=user.is_superuser,
            is_hotel_admin=user.is_hotel_admin,
        )
