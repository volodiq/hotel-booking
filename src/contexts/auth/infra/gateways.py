from dataclasses import dataclass

from contexts.users.api.internal import VerifyUserPassword

from ..core.gateways import UsersGateway, VerifyUserPasswordOut


@dataclass
class InternalUsersGateway(UsersGateway):
    verify_user_password_api: VerifyUserPassword

    async def verify_user_password(
        self,
        raw_phone: str,
        raw_password: str,
    ) -> VerifyUserPasswordOut:
        raw_data = await self.verify_user_password_api(
            raw_phone=raw_phone,
            raw_password=raw_password,
        )
        return VerifyUserPasswordOut(
            is_valid=raw_data.is_valid,
            user_oid=raw_data.user_oid,
            is_superuser=raw_data.is_superuser,
        )
