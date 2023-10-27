from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass


@dataclass
class Token():
    access_token: str
    token_type: str


@dataclass
class TokenData():
    username: Optional[str] = None
    scopes: List[str] = field(default_factory=lambda: [])
