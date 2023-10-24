from datetime import date

from pydantic import BaseModel


class LoginReq(BaseModel):
    id: int
    username: str
    password: str
    date_approved: date
    user_type: int

    class Config:
        orm_mode = True
