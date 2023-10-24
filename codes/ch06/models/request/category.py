from datetime import date
from typing import List, Any, Optional

from pydantic import BaseModel


class CategoryReq(BaseModel):
    id: int
    name: str
    description: str
    date_added: date


class ReferenceReq(BaseModel):
    id: int
    name: str
    description: str
    date_added: date
    categories: List[Any] = list()


class BookReq(BaseModel):
    id: int
    isbn: str
    author: str
    title: str
    edition: int
    date_published: date
    price: float
    category: Optional[CategoryReq] = None
