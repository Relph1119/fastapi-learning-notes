from datetime import date

from pydantic import BaseModel


class OrderReq(BaseModel):
    id: int
    user_id: int
    date_ordered: date


class ReceiptReq(BaseModel):
    id: int
    date_receipt: date
    total: float
    payment_mode: int
    order_id: int


class CartReq(BaseModel):
    id: int
    book_id: int
    user_id: int
    qty: int
    date_carted: date
    discount: float
