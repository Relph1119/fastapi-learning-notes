from datetime import date

from pydantic import BaseModel


class VendorReq(BaseModel):
    id: int
    rep_firstname: str
    rep_lastname: str
    rep_id: str
    rep_date_employed: date
    account_name: str
    account_number: str
    date_consigned: date
    login_id: int
