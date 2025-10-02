from dishka import Provider, Scope

from .core import use_cases
from .core.gateways import UsersGateway
from .infra.gateways import InternalUsersGateway


auth_provider = Provider()
auth_provider.provide(InternalUsersGateway, provides=UsersGateway, scope=Scope.REQUEST)
auth_provider.provide(use_cases.AuthenticateUser, scope=Scope.REQUEST)
auth_provider.provide(use_cases.RefreshToken, scope=Scope.REQUEST)
