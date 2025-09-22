from pydantic import BaseModel


class SLoginIn(BaseModel):
    phone: str
    password: str


class SLoginOut(BaseModel):
    access_token: str
    refresh_token: str
