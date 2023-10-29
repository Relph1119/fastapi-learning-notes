from datetime import date

from pydantic import BaseModel

from models.data.ratings_enum import FoodRatingScale


class FoodRateReq(BaseModel):
    rate: FoodRatingScale
    date_rated: date
    profile_id: int
