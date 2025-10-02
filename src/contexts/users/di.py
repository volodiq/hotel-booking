from dishka import Provider, Scope

from .api.internal import VerifyUserPassword
from .core import use_cases
from .infra.repositories import SAUserRepository, UserRepository


users_provider = Provider()
users_provider.provide(SAUserRepository, provides=UserRepository, scope=Scope.REQUEST)
users_provider.provide(VerifyUserPassword, scope=Scope.REQUEST)
users_provider.provide(use_cases.CreateUser, scope=Scope.REQUEST)
users_provider.provide(use_cases.GetUserByPhoneAndPassword, scope=Scope.REQUEST)
users_provider.provide(use_cases.MakeHotelAdmin, scope=Scope.REQUEST)
