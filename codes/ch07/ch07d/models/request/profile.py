from datetime import date

from pydantic import BaseModel


class ProfileReq(BaseModel):
    id: int
    firstname: str
    lastname: str
    age: int
    membership_date: date
    member_type: str
    login_id: int
    status: int
