from datetime import date
from typing import Optional

from pydantic import BaseModel


class RestaurantReq(BaseModel):
    restaurant_id: int
    name: str
    branch: Optional[str] = None
    address: str
    province: str
    date_signed: date
    city: str
    country: str
    zipcode: int
