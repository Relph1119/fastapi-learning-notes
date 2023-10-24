# No need for models

from dataclasses import field
from datetime import date, datetime
from typing import List, Optional

from bson import ObjectId
from pydantic import field_validator
from pydantic.dataclasses import dataclass


class Config:
    arbitrary_types_allowed = True


@dataclass(config=Config)
class PurchaseHistory:
    purchase_id: Optional[int] = None
    shipping_address: Optional[str] = None
    email: Optional[str] = None
    date_purchased: Optional[date] = "1900-01-01T00:00:00"
    date_shipped: Optional[date] = "1900-01-01T00:00:00"
    date_payment: Optional[date] = "1900-01-01T00:00:00"

    @field_validator('date_purchased', mode='before')
    def date_purchased_datetime(cls, value):
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date()

    @field_validator('date_shipped', mode='before')
    def date_shipped_datetime(cls, value):
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date()

    @field_validator('date_payment', mode='before')
    def date_payment_datetime(cls, value):
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date()


@dataclass(config=Config)
class PurchaseStatus:
    status_id: Optional[int] = None
    name: Optional[str] = None
    discount: Optional[float] = None
    date_membership: Optional[date] = "1900-01-01T00:00:00"

    @field_validator('date_membership', mode='before')
    def date_membership_datetime(cls, value):
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date()


@dataclass(config=Config)
class Buyer:
    buyer_id: int
    user_id: int
    date_purchased: date
    purchase_history: List[PurchaseHistory] = field(default_factory=list)
    customer_status: Optional[PurchaseStatus] = field(default_factory=dict)
    _id: ObjectId = field(default=ObjectId())

    @field_validator('date_purchased', mode='before')
    def date_purchased_datetime(cls, value):
        print(type(value))
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date()
