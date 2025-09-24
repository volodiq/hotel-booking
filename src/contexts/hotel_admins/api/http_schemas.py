from pydantic import BaseModel


class SCreateHotelAdmin(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    phone: str
    raw_password: str
    email: str
