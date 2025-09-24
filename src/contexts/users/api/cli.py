import asyncclick
from dishka.integrations.click import FromDishka

from shared.providers.env import Env
from utils.asyncclick_dishka import cli_inject

from ..core.services import CreateUserService


@asyncclick.command()
@asyncclick.option("--phone", prompt="Enter the phone")
@asyncclick.option("--name", prompt="Enter the name")
@asyncclick.option("--last_name", prompt="Enter the last name")
@asyncclick.option("--password", prompt="Enter the password")
@cli_inject
async def create_superuser(
    phone: str,
    name: str,
    last_name: str,
    password: str,
    env: FromDishka[Env],
    create_user_service: FromDishka[CreateUserService],
):
    print(env.db_dsn)
    await create_user_service(
        first_name=name,
        last_name=last_name,
        phone=phone,
        password=password,
        is_superuser=True,
    )
    print("Superuser created")
