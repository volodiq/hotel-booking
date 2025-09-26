from dishka import Provider, Scope, provide

from app.container import make_container
from system.security.dtos import Principal


class PrincipalProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def principal(self) -> Principal:
        raise NotImplementedError("PrincipalProvider не должен использоваться в CLI-контексте")


container = make_container(PrincipalProvider())
