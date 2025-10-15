"""
Файл нужен для инициализации всех моделей.
"""

from contexts.hotels.infra.models import HotelModel, RoomModel, RoomPhotoModel
from contexts.users.infra.models import UserModel
from shared.infra.models import DBModel


__all__ = [
    "DBModel",
    "UserModel",
    "RoomModel",
    "RoomPhotoModel",
    "HotelModel",
]
