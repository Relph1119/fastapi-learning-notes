from datetime import date

from pydantic import BaseModel


class ProfileReq(BaseModel):
    firstname: str
    lastname: str
    middlename: str
    date_signed: date
    age: int
    date_signed: date
    occupation: str
    birthday: date
    address: str
