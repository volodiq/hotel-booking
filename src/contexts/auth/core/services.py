from abc import ABC, abstractmethod
from dataclasses import dataclass

from . import errors
from .dtos import TokenPair
from .gateways import UsersGateway


@dataclass
class TokenService(ABC):
    @abstractmethod
    def create_token_pair(self, user_oid: str) -> TokenPair: ...


@dataclass
class AuthenticateUserService:
    users_gateway: UsersGateway
    token_service: TokenService

    async def __call__(self, phone: str, password: str) -> TokenPair:
        verification_result = await self.users_gateway.verify_user_password(phone, password)
        if verification_result.user_oid is None or not verification_result.is_valid:
            raise errors.InvalidCredentials()

        return self.token_service.create_token_pair(verification_result.user_oid)
