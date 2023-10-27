from datetime import date

from pydantic import BaseModel


class BidsReq(BaseModel):
    id: int
    auction_id: int
    profile_id: int
    created_date: date
    updated_date: date
    price: float
