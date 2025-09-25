from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from contexts.auth.api.http_router import router as auth_router
from contexts.hotel_admins.api.http_router import router as hotel_admins_router
from contexts.users.api.http_router import router as users_router


router = APIRouter(route_class=DishkaRoute)
router.include_router(auth_router)
router.include_router(hotel_admins_router)
router.include_router(users_router)
