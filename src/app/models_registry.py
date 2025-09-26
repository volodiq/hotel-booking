"""
Файл нужен для инициализации всех моделей.
"""

from contexts.users.infra.models import UserModel
from shared.infra.models import DBModel


__all__ = [
    "DBModel",
    "UserModel",
]
