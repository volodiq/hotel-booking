from sqlalchemy import sql

from shared.infra.repositories import SARepository

from ..core import entities, repositories, values
from . import models


class SAHotelAdminRepository(repositories.HotelAdminRepository, SARepository[models.HotelAdmin]):
    async def create_hotel_admin(self, hotel_admin: entities.HotelAdmin):
        model = models.HotelAdmin(
            oid=hotel_admin.oid,
            first_name=hotel_admin.first_name.value,
            last_name=hotel_admin.last_name.value,
            middle_name=hotel_admin.middle_name.value,
            phone=hotel_admin.phone.value,
            email=hotel_admin.email.value,
            password_hash=hotel_admin.password_hash,
            is_banned=hotel_admin.is_banned,
            created_at=hotel_admin.created_at,
        )
        self.create(model)

    async def get_hotel_admin_by_phone(self, phone: str) -> entities.HotelAdmin | None:
        stmt = sql.select(models.HotelAdmin).where(models.HotelAdmin.phone == phone)
        res = await self.session.scalars(stmt)
        hotel_admin_db = res.one_or_none()
        if not hotel_admin_db:
            return None

        return entities.HotelAdmin(
            oid=hotel_admin_db.oid,
            first_name=values.FirstName(hotel_admin_db.first_name),
            last_name=values.LastName(hotel_admin_db.last_name),
            middle_name=values.MiddleName(hotel_admin_db.middle_name),
            phone=values.PhoneNumber(hotel_admin_db.phone),
            email=values.Email(hotel_admin_db.email),
            password_hash=hotel_admin_db.password_hash,
            is_banned=hotel_admin_db.is_banned,
            created_at=hotel_admin_db.created_at,
        )

    async def update_hotel_admin(self, hotel_admin: entities.HotelAdmin):
        stmt = (
            sql.update(models.HotelAdmin)
            .where(models.HotelAdmin.oid == hotel_admin.oid)
            .values(
                {
                    "first_name": hotel_admin.first_name.value,
                    "last_name": hotel_admin.last_name.value,
                    "middle_name": hotel_admin.middle_name.value,
                    "phone": hotel_admin.phone.value,
                    "email": hotel_admin.email.value,
                    "password_hash": hotel_admin.password_hash,
                    "is_banned": hotel_admin.is_banned,
                    "created_at": hotel_admin.created_at,
                }
            )
        )
        await self.session.execute(stmt)
