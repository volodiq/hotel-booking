from dataclasses import dataclass

from shared.providers.security import Principal, TokenService, TokenType

from . import errors
from .gateways import UsersGateway


@dataclass
class TokenPair:
    access_token: str
    refresh_token: str


@dataclass
class AuthenticateUserService:
    users_gateway: UsersGateway
    token_service: TokenService

    async def __call__(self, phone: str, password: str) -> TokenPair:
        verification_result = await self.users_gateway.verify_user_password(phone, password)
        if verification_result.user_oid is None or not verification_result.is_valid:
            raise errors.InvalidCredentials()

        principal = Principal(sub=verification_result.user_oid, roles=["user"])
        access = self.token_service.encode(principal, TokenType.ACCESS)
        refresh = self.token_service.encode(principal, TokenType.REFRESH)
        return TokenPair(access_token=access, refresh_token=refresh)


@dataclass
class RefreshTokenService:
    token_service: TokenService

    async def __call__(self, refresh_token: str) -> str:
        principal = self.token_service.decode(refresh_token, TokenType.REFRESH)
        return self.token_service.encode(principal, TokenType.ACCESS)
