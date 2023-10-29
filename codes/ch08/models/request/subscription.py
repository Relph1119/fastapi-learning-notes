from datetime import date

from pydantic import BaseModel


class SubscriptionReq(BaseModel):
    id: int
    customer_id: int
    branch: str
    price: float
    qty: int
    date_purchased: date
