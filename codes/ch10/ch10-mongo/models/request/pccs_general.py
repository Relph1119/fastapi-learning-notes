from typing import Dict

from pydantic import BaseModel


class SurveyDataResult(BaseModel):
    results: Dict[str, int]
