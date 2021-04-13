from enum import Enum

from pydantic import BaseModel


class ProductSerializer(BaseModel):
    name: str
    description: str
    stock: float


class DocumentType(str, Enum):
    ni = "NI"
    ti = "TI"
    cc = "CC"
    pa = "PA"
    ce = "CE"
    rc = "RC"
    cd = "CD"
    pe = "PE"


class Item:
    name: str

    def __init__(self, name: str):
        self.name = name
