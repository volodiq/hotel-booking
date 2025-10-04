from dishka import Provider, Scope

from contexts.auth.app import use_cases as auth_use_cases
from contexts.auth.infra import gateways as auth_gateways
from contexts.users.api import internal as users_internal
from contexts.users.app import use_cases as users_use_cases
from contexts.users.infra import repositories as users_repositories
from system.security.passwords.services import BcryptPasswordService, PasswordService

from . import providers


provider = Provider()

# Common
provider.provide(providers.get_env, scope=Scope.APP)
provider.provide(providers.get_session_pool, scope=Scope.APP)
provider.provide(providers.get_token_service, scope=Scope.APP)
provider.provide(providers.get_sa_session, scope=Scope.REQUEST)
provider.provide(BcryptPasswordService, provides=PasswordService, scope=Scope.APP)


# Auth
provider.provide(auth_use_cases.AuthenticateUser, scope=Scope.REQUEST)
provider.provide(auth_use_cases.RefreshToken, scope=Scope.REQUEST)
provider.provide(
    auth_gateways.InternalUsersGateway,
    provides=auth_gateways.UsersGateway,
    scope=Scope.REQUEST,
)

# Users
provider.provide(users_use_cases.CreateUser, scope=Scope.REQUEST)
provider.provide(users_use_cases.MakeHotelAdmin, scope=Scope.REQUEST)
provider.provide(users_use_cases.GetUserByPhoneAndPassword, scope=Scope.REQUEST)
provider.provide(users_internal.VerifyUserPassword, scope=Scope.REQUEST)
provider.provide(
    users_repositories.SAUserRepository,
    provides=users_repositories.UserRepository,
    scope=Scope.REQUEST,
)
