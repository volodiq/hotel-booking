from dishka import Provider, Scope

from .api.internal import VerifyUserPassword
from .core.services import CreateUserService, GetUserByPhoneAndPasswordService, PasswordHashService
from .infra.repositories import SAUserRepository, UserRepository
from .infra.services import SHA256PasswordHashService


users_provider = Provider()
users_provider.provide(SHA256PasswordHashService, provides=PasswordHashService, scope=Scope.APP)
users_provider.provide(SAUserRepository, provides=UserRepository, scope=Scope.REQUEST)
users_provider.provide(VerifyUserPassword, scope=Scope.REQUEST)
users_provider.provide(CreateUserService, scope=Scope.REQUEST)
users_provider.provide(GetUserByPhoneAndPasswordService, scope=Scope.REQUEST)
