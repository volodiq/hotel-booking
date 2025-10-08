"""
Файл нужен для инициализации всех моделей.
"""

from contexts.hotels.infra.models import Hotel, Room, RoomPhoto
from contexts.users.infra.models import UserModel
from shared.infra.models import DBModel


__all__ = [
    "DBModel",
    "UserModel",
    "Room",
    "RoomPhoto",
    "Hotel",
]
