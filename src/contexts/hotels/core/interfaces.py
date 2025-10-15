from abc import ABC, abstractmethod

from . import entities


class HotelRepository(ABC):
    @abstractmethod
    async def save(self, hotel: entities.Hotel): ...

    @abstractmethod
    async def get_by_oid(self, oid: str) -> entities.Hotel | None: ...


class RoomRepository(ABC):
    @abstractmethod
    async def save(self, room: entities.Room): ...

    @abstractmethod
    async def get_by_oid(self, oid: str) -> entities.Room | None: ...


class PhotoStorage(ABC):
    @abstractmethod
    async def upload(self, photo_as_bytes: bytes) -> str: ...
