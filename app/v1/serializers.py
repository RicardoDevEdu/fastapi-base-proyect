from enum import Enum
from typing import List

from pydantic import BaseModel


class ProductSerializer(BaseModel):
    name: str
    description: str
    stock: float

class MetaPaginate(BaseModel):
    current_page: int
    item_per_page: int
    total_page: int
    available_orders: List
class BasePaginate(BaseModel):
    data: List
    meta: MetaPaginate
class User(BaseModel): 
    name: str
    last_name: str
    email: str
    address: List

class UserPaginate(BasePaginate):
    data: List[User]