import asyncclick
from dishka.integrations.click import FromDishka

from shared.api.click_di import cli_inject

from ..core import use_cases


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
    create_user_service: FromDishka[use_cases.CreateUser],
):
    await create_user_service(
        first_name=name,
        last_name=last_name,
        phone=phone,
        password=password,
        is_superuser=True,
    )
    print("Superuser created")
