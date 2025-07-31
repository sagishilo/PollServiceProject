from typing import Optional
from pydantic.main import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    age: int
    address: str
    is_registered: bool = False