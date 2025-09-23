from datetime import timedelta

from dishka import Provider, Scope, provide

from contexts.users.api.internal import VerifyUserPassword
from shared.providers.env import Env

from .core.gateways import UsersGateway
from .core.services import AuthenticateUserService, RefreshTokenService, TokenService
from .infra import gateways, services


class AuthProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def token_service(self, env: Env) -> TokenService:
        return services.PyJWTTokenService(
            secret_key=env.SECRET_KEY,
            access_token_ttl=timedelta(hours=1),
            refresh_token_ttl=timedelta(weeks=1),
        )

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
    async def refresh_token_service(
        self,
        token_service: TokenService,
    ) -> RefreshTokenService:
        return RefreshTokenService(token_service=token_service)
