from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from .api.internal import VerifyUserPassword
from .core.services import CreateUserService, PasswordHashService
from .infra.repositories import SAUserRepository, UserRepository
from .infra.services import SHA256PasswordHashService


class UsersProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def user_repository(self, session: AsyncSession) -> UserRepository:
        return SAUserRepository(session)

    @provide(scope=Scope.REQUEST)
    async def create_user_service(
        self,
        repository: UserRepository,
        password_hash_service: PasswordHashService,
    ) -> CreateUserService:
        return CreateUserService(
            repository=repository,
            password_hash_service=password_hash_service,
        )

    @provide(scope=Scope.REQUEST)
    async def verify_user_password_service(
        self,
        user_repository: UserRepository,
        password_hash_service: PasswordHashService,
    ) -> VerifyUserPassword:
        return VerifyUserPassword(
            user_repository=user_repository,
            password_hash_service=password_hash_service,
        )

    @provide(scope=Scope.APP)
    async def hash_service(self) -> PasswordHashService:
        return SHA256PasswordHashService()
