from datetime import date

from pydantic import BaseModel


class QuestionReq(BaseModel):
    question_id: int
    statement: str
    date_added: date
    profile_id: int
