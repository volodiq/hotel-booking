from dishka import Provider, Scope

from .core.gateways import UsersGateway
from .core.services import AuthenticateUserService, RefreshTokenService
from .infra.gateways import InternalUsersGateway


auth_provider = Provider()
auth_provider.provide(InternalUsersGateway, provides=UsersGateway, scope=Scope.REQUEST)
auth_provider.provide(AuthenticateUserService, scope=Scope.REQUEST)
auth_provider.provide(RefreshTokenService, scope=Scope.REQUEST)
