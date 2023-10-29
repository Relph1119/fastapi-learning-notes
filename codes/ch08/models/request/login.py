from pydantic import BaseModel


class LoginReq(BaseModel):
    id: int
    username: str
    password: str
    user_type: int
