from datetime import date

from pydantic import BaseModel


class SalesReq(BaseModel):
    id: int
    publication_id: int
    copies_issued: int
    copies_sold: int
    date_issued: date
    revenue: float
    profit: float
