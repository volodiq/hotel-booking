from dishka import Provider, Scope

from .api.internal import VerifyUserPassword
from .core.services import (
    CreateUserService,
    GetUserByPhoneAndPasswordService,
    MakeHotelAdminService,
)
from .infra.repositories import SAUserRepository, UserRepository


users_provider = Provider()
users_provider.provide(SAUserRepository, provides=UserRepository, scope=Scope.REQUEST)
users_provider.provide(VerifyUserPassword, scope=Scope.REQUEST)
users_provider.provide(CreateUserService, scope=Scope.REQUEST)
users_provider.provide(GetUserByPhoneAndPasswordService, scope=Scope.REQUEST)
users_provider.provide(MakeHotelAdminService, scope=Scope.REQUEST)
