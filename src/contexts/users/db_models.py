from sqlalchemy.orm import Mapped, mapped_column

from shared.infra.db_models import DBModel
from shared.infra.domains import String


class UserModel(DBModel):
    __tablename__ = "users"

    first_name: Mapped[String]
    last_name: Mapped[String]
    phone_number: Mapped[String] = mapped_column(index=True)
