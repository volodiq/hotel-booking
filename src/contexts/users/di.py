from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from .core.services import CreateUserService
from .infra.repositories import SAUserRepository, UserRepository


class UsersProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def provide_user_repository(self, session: AsyncSession) -> UserRepository:
        return SAUserRepository(session)

    @provide(scope=Scope.REQUEST)
    async def provide_create_user_service(self, repository: UserRepository) -> CreateUserService:
        return CreateUserService(repository)
