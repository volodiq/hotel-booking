from sqlalchemy import types
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from shared.infra.db_domains import DateTime


class DBModel(DeclarativeBase):
    oid: Mapped[str] = mapped_column(types.UUID, primary_key=True)
    created_at: Mapped[DateTime]
