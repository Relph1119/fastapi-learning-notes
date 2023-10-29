from datetime import date

from pydantic import BaseModel


class MessengerReq(BaseModel):
    id: int
    firstname: str
    lastname: str
    salary: float
    date_employed: date
    status: int
    vendor_id: int
