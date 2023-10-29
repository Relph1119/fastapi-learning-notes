from datetime import date

from pydantic import BaseModel


class CustomerReq(BaseModel):
    id: int
    firstname: str
    lastname: str
    age: int
    birthday: date
    date_subscribed: date
    status: int
    subscription_type: int
    login_id: int
