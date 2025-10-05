from pydantic import BaseModel, Field


class SCreateUser(BaseModel):
    phone: str = Field(examples=["+7 999 999 99 99"])
    first_name: str = Field(examples=["John"])
    last_name: str = Field(examples=["Doe"])
    password: str


class SVerifyUserPasswordOut(BaseModel):
    is_valid: bool
    user_oid: str | None = None
    is_superuser: bool | None = None
    is_hotel_admin: bool | None = None
