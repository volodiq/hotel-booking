from datetime import timedelta

from dishka import Provider, Scope

from contexts.auth.app import use_cases as auth_use_cases
from contexts.auth.infra import gateways as auth_gateways
from contexts.users.api import internal as users_internal
from contexts.users.app import use_cases as users_use_cases
from contexts.users.infra import repositories as users_repositories
from shared.infra import services as common_services

from . import db, env


provider = Provider()


# SQLAlchemy
provider.provide(db.SessionProvider.from_env, scope=Scope.APP)
provider.provide(db.SessionProvider.get_session, scope=Scope.REQUEST)

# Env
provider.provide(env.get_env, scope=Scope.APP)

# Common
provider.provide(
    common_services.BcryptPasswordService,
    provides=common_services.PasswordService,
    scope=Scope.APP,
)


def get_token_service(env: env.Env) -> common_services.TokenService:
    return common_services.PyJWTTokenService(
        secret_key=env.SECRET_KEY,
        access_token_ttl=timedelta(hours=1),
        refresh_token_ttl=timedelta(weeks=1),
    )


provider.provide(get_token_service, scope=Scope.APP)

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
