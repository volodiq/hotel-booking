"""
Файл нужен для инициализации всех моделей.
"""

from contexts.users.db_models import UserModel
from shared.infra.db_models import DBModel


__all__ = [
    "DBModel",
    "UserModel",
]
