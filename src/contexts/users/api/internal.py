from dataclasses import dataclass

from ..app import use_cases
from . import schemas


@dataclass
class VerifyUserPassword:
    use_case: use_cases.GetUserByPhoneAndPassword

    async def __call__(
        self,
        raw_phone: str,
        raw_password: str,
    ) -> schemas.SVerifyUserPasswordOut:
        user = await self.use_case(raw_phone, raw_password)
        if user is None:
            return schemas.SVerifyUserPasswordOut(is_valid=False)

        return schemas.SVerifyUserPasswordOut(
            is_valid=True,
            user_oid=user.oid,
            is_superuser=user.is_superuser,
            is_hotel_admin=user.is_hotel_admin,
        )
