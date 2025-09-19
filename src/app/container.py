from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider

from providers.db import DBSessionPoolProvider, DBSessionProvider
from providers.env import EnvProvider


container = make_async_container(
    FastapiProvider(),
    EnvProvider(),
    DBSessionPoolProvider(),
    DBSessionProvider(),
)
