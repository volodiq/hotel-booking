from dataclasses import dataclass

from shared.core.dtos import Principal

from . import errors, interfaces


@dataclass
class HotelAccessService:
    hotel_repository: interfaces.HotelRepository

    def verify_module_access(self, principal: Principal) -> None:
        if "hotel_admin" not in principal.roles:
            raise errors.ActionForbidden()

    async def verify_hotel_access(self, principal: Principal, hotel_oid: str) -> None:
        self.verify_module_access(principal=principal)

        hotel = await self.hotel_repository.get_by_oid(hotel_oid)
        if hotel is None or hotel.hotel_admin_oid != principal.sub:
            raise errors.HotelNotFound()
