from sqlalchemy.orm import Mapped, mapped_column

from shared.infra.db_domains import Bool, String
from shared.infra.models import DBModel


class UserModel(DBModel):
    __tablename__ = "users"

    first_name: Mapped[String]
    last_name: Mapped[String]
    phone_number: Mapped[String] = mapped_column(index=True)
    password_hash: Mapped[String]
    is_superuser: Mapped[Bool]
    is_hotel_admin: Mapped[Bool]
