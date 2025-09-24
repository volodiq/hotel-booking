from dishka import Provider, Scope, provide

from contexts.users.api.internal import VerifyUserPassword
from shared.providers.security import TokenService

from .core.gateways import UsersGateway
from .core.services import AuthenticateUserService, RefreshTokenService
from .infra import gateways


class AuthProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def users_gateway(
        self,
        verify_user_password_api: VerifyUserPassword,
    ) -> UsersGateway:
        return gateways.InternalUsersGateway(verify_user_password_api)

    @provide(scope=Scope.REQUEST)
    async def authenticate_user_service(
        self,
        users_gateway: UsersGateway,
        token_service: TokenService,
    ) -> AuthenticateUserService:
        return AuthenticateUserService(
            users_gateway=users_gateway,
            token_service=token_service,
        )

    @provide(scope=Scope.REQUEST)
    async def refresh_token_service(self, token_service: TokenService) -> RefreshTokenService:
        return RefreshTokenService(token_service=token_service)
