from pydantic import BaseModel

from ..core import entities


class SCreateHotel(BaseModel):
    rating: int
    name: str
    address: str


class SCreateRoom(BaseModel):
    name: str
    description: str
    room_type: entities.RoomType
    bed_type: entities.RoomBedType
