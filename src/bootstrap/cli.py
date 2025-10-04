import asyncclick
from dishka import make_async_container
from dishka.integrations.click import setup_dishka

from bootstrap.container import provider
from contexts.users.api.cli import create_superuser
from shared.core.errors import DomainError


@asyncclick.group()
@asyncclick.pass_context
def main(context: asyncclick.Context):
    container = make_async_container(provider)
    setup_dishka(container=container, context=context)  # type: ignore


main.add_command(cmd=create_superuser, name="createsuperuser")


if __name__ == "__main__":
    try:
        main()
    except DomainError as e:
        print(f"Ошибка: {e.details}")
