import asyncclick
from dishka.integrations.click import setup_dishka

from app.container import container
from contexts.users.api.cli import create_superuser
from system.seedwork.errors import DomainError


@asyncclick.group()
@asyncclick.pass_context
def main(context: asyncclick.Context):
    setup_dishka(container=container, context=context)  # type: ignore


main.add_command(cmd=create_superuser, name="createsuperuser")


if __name__ == "__main__":
    try:
        main()
    except DomainError as e:
        print(f"Ошибка: {e.details}")
