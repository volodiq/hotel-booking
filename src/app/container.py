from dishka import AsyncContainer, Provider, make_async_container

from contexts.auth.di import auth_provider
from contexts.users.di import users_provider
from system.di import system_provider


PROVIDERS: tuple[Provider, ...] = (
    system_provider,
    users_provider,
    auth_provider,
)


def make_container(principal_provider: Provider, *providers: Provider) -> AsyncContainer:
    """
    Создает DI контейнер.

    principal_provider - провайдер для получения Principal
    (или вызов исключения, если авторизация не поддерживается интерфейсом).

    providers - дополнительные провайдеры.
    """

    return make_async_container(
        principal_provider,
        *PROVIDERS,
        *providers,
    )
