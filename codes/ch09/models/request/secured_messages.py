from pydantic import BaseModel


class EncLoginReq(BaseModel):
    enc_login: str
    key: str


class EncRestaurantReq(BaseModel):
    enc_login: str
    key: str
