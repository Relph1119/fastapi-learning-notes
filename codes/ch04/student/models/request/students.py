from typing import Optional

from models.data.students import StudentStatus, Major
from pydantic import BaseModel


class SignupReq(BaseModel):
    stud_id: int
    username: str
    password: str


class StudentReq(BaseModel):
    stud_id: int
    fname: str
    lname: str
    mname: str
    age: int
    major: Major
    department: str
    status: StudentStatus


class StudentDetails(BaseModel):
    fname: Optional[str] = None
    lname: Optional[str] = None
    mname: Optional[str] = None
    age: Optional[int] = None
    major: Optional[Major] = None
    department: Optional[str] = None
    status: Optional[StudentStatus] = None
