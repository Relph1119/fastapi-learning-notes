from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AssignmentRequest(BaseModel):
    bin_id: int
    assgn_id: int
    title: str
    date_completed: Optional[datetime] = None
    date_due: datetime
    rating: Optional[float] = None
    course: str
