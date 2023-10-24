from datetime import datetime
from typing import Optional

from models.data.library import Classification
from pydantic import BaseModel


class BookReq(BaseModel):
    book_id: int
    title: str
    classification: Classification
    author: str
    year_published: datetime
    edition: int


class BookDetails(BaseModel):
    title: Optional[str] = None
    classification: Optional[Classification] = None
    author: Optional[str] = None
    year_published: Optional[datetime] = None
    edition: Optional[int] = None


class BookRequestReq(BaseModel):
    book_id: int
    request_date: datetime
    status: bool


class BookIssuanceReq(BaseModel):
    req_id: int
    approved_by: str
    approved_date: datetime


class BookReturnReq(BaseModel):
    issue_id: int
    returned_date: datetime
