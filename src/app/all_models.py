"""
Файл нужен для инициализации всех моделей.
"""

from contexts.users.db_models import UserModel
from core.db.models import DBModel


__all__ = [
    "DBModel",
    "UserModel",
]
