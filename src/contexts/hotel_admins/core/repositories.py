from abc import ABC, abstractmethod

from . import entities


class HotelAdminRepository(ABC):
    @abstractmethod
    async def create_hotel_admin(self, hotel_admin: entities.HotelAdmin): ...

    @abstractmethod
    async def get_hotel_admin_by_phone(self, phone: str) -> entities.HotelAdmin | None: ...

    @abstractmethod
    async def update_hotel_admin(self, hotel_admin: entities.HotelAdmin): ...
