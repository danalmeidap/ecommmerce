from typing import  Optional
from pydantic import BaseModel
from datetime import datetime


class Product(BaseModel):
    id: Optional[int] = None
    name:str
    price:float
    score:int
    created: datetime

    class config:
        orm_mode = True

