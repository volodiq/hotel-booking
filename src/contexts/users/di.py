from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from .api.internal import VerifyUserPassword
from .core.services import CreateUserService
from .infra.repositories import SAUserRepository, UserRepository


class UsersProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def user_repository(self, session: AsyncSession) -> UserRepository:
        return SAUserRepository(session)

    @provide(scope=Scope.REQUEST)
    async def create_user_service(self, repository: UserRepository) -> CreateUserService:
        return CreateUserService(repository)

    @provide(scope=Scope.REQUEST)
    async def verify_user_password_service(
        self,
        user_repository: UserRepository,
    ) -> VerifyUserPassword:
        return VerifyUserPassword(user_repository)
