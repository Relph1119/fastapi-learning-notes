from datetime import date

from pydantic import BaseModel


class FeedbackReq(BaseModel):
    message: str
    date_rated: date
    profile_id: int
