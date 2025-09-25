from dishka import Provider, Scope

from .core.repositories import HotelAdminRepository
from .core.services import CreateHotelAdminService, PasswordHashService
from .infra.repositories import SAHotelAdminRepository
from .infra.services import SHA256PasswordHashService


hotel_admin_provider = Provider()
hotel_admin_provider.provide(
    SAHotelAdminRepository,
    provides=HotelAdminRepository,
    scope=Scope.REQUEST,
)
hotel_admin_provider.provide(
    SHA256PasswordHashService,
    provides=PasswordHashService,
    scope=Scope.APP,
)
hotel_admin_provider.provide(CreateHotelAdminService, scope=Scope.REQUEST)
