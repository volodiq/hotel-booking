from pydantic import BaseModel, Field


class SCreateUser(BaseModel):
    phone: str = Field(examples=["+7 999 999 99 99"])
    first_name: str = Field(examples=["John"])
    last_name: str = Field(examples=["Doe"])
