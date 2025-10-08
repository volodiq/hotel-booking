from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from shared.infra.db_domains import UUID, DateTime


class DBModel(DeclarativeBase):
    oid: Mapped[UUID] = mapped_column(primary_key=True)
    created_at: Mapped[DateTime]
