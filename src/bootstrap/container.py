from dishka import Provider, Scope

from contexts.auth.app import use_cases as auth_use_cases
from contexts.auth.infra import gateways as auth_gateways
from contexts.hotels.app import use_cases as hotels_use_cases
from contexts.hotels.infra import gateways as hotels_gateways, repositories as hotels_repositories
from contexts.users.api import internal as users_internal
from contexts.users.app import use_cases as users_use_cases
from contexts.users.infra import repositories as users_repositories
from shared.infra import services as common_services

from . import config, db


provider = Provider(scope=Scope.REQUEST)


# Common
provider.provide(db.get_session)
provider.provide(
    common_services.BcryptPasswordService,
    provides=common_services.PasswordService,
    scope=Scope.APP,
)


def get_token_service() -> common_services.TokenService:
    return common_services.PyJWTTokenService(
        secret_key=config.secret_key,
        access_token_ttl=config.access_token_ttl,
        refresh_token_ttl=config.refresh_token_ttl,
    )


provider.provide(get_token_service, scope=Scope.APP)

# Auth
provider.provide(auth_use_cases.RefreshToken)
provider.provide(auth_use_cases.AuthenticateUser)
provider.provide(auth_gateways.InternalUsersGateway, provides=auth_gateways.UsersGateway)

# Users
provider.provide(users_use_cases.CreateUser)
provider.provide(users_use_cases.MakeHotelAdmin)
provider.provide(users_internal.VerifyUserPassword)
provider.provide(users_use_cases.GetUserByPhoneAndPassword)
provider.provide(users_repositories.SAUserRepository, provides=users_repositories.UserRepository)

# Hotels
provider.provide(hotels_use_cases.CreateHotel)
provider.provide(hotels_use_cases.CreateRoom)
provider.provide(hotels_use_cases.AddRoomPhoto)

# TODO s3 session
provider.provide(
    hotels_repositories.SAHotelRepository,
    provides=hotels_repositories.HotelRepository,
)
provider.provide(hotels_gateways.MockPhotoStorage, provides=hotels_gateways.PhotoStorage)
provider.provide(hotels_repositories.SARoomRepository, provides=hotels_repositories.RoomRepository)
