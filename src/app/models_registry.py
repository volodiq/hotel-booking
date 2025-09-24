"""
Файл нужен для инициализации всех моделей.
"""

from contexts.hotel_admins.infra.models import HotelAdmin
from contexts.users.infra.models import UserModel
from shared.infra.models import DBModel


__all__ = [
    "DBModel",
    "UserModel",
    "HotelAdmin",
]
