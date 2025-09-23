from sqlalchemy.orm import Mapped, mapped_column

from shared.infra import db_domains
from shared.infra.models import DBModel


class HotelAdmin(DBModel):
    __tablename__ = "hotel_admins"

    first_name: Mapped[db_domains.String]
    last_name: Mapped[db_domains.String]
    middle_name: Mapped[db_domains.String]
    phone: Mapped[db_domains.String] = mapped_column(index=True)
    email: Mapped[db_domains.String]
    password_hash: Mapped[db_domains.String]
    is_banned: Mapped[db_domains.Bool]
