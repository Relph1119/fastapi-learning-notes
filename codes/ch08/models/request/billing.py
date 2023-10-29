from datetime import date

from pydantic import BaseModel


class BillingReq(BaseModel):
    id: int
    payable: float
    approved_by: str
    date_approved: date
    date_billed: date
    received_by: str
    date_received: date
    total_issues: int
    vendor_id: int
    admin_id: int
