import asyncclick
from dishka import Scope
from dishka.integrations.base import wrap_injection
from dishka.integrations.click import CONTAINER_NAME


def cli_inject(func):
    """
    Декоратор для внедрения зависимостей в asyncclick.
    """

    return wrap_injection(
        func=func,
        container_getter=lambda _, __: asyncclick.get_current_context().meta[CONTAINER_NAME],
        remove_depends=True,
        is_async=True,
        scope=Scope.REQUEST,
    )
