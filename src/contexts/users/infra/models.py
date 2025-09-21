from sqlalchemy.orm import Mapped, mapped_column

from shared.infra.db_domains import String
from shared.infra.models import DBModel


class UserModel(DBModel):
    __tablename__ = "users"

    first_name: Mapped[String]
    last_name: Mapped[String]
    phone_number: Mapped[String] = mapped_column(index=True)
