from datetime import date

from pydantic import BaseModel


class AttendanceMemberReq(BaseModel):
    id: int
    member_id: int
    timeout: int
    timein: int
    date_log: date
