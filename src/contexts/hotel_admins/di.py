from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from shared.providers.security import Principal

from .core.repositories import HotelAdminRepository
from .core.services import CreateHotelAdminService, PasswordHashService
from .infra.repositories import SAHotelAdminRepository
from .infra.services import SHA256PasswordHashService


class HotelAdminProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def hotel_admin_repository(self, session: AsyncSession) -> HotelAdminRepository:
        return SAHotelAdminRepository(session)

    @provide(scope=Scope.APP)
    async def hash_service(self) -> PasswordHashService:
        return SHA256PasswordHashService()

    @provide(scope=Scope.REQUEST)
    async def create_hotel_admin_service(
        self,
        hotel_admin_repository: HotelAdminRepository,
        password_hash_service: PasswordHashService,
        principal: Principal,
    ) -> CreateHotelAdminService:
        return CreateHotelAdminService(
            hotel_admin_repository=hotel_admin_repository,
            password_hash_service=password_hash_service,
            principal=principal,
        )
