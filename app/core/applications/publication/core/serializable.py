from typing import List, Optional
from pydantic.main import BaseModel


class Author(BaseModel):
    name: str
    mode: Optional[str]
    uuid: str


class Image(BaseModel):
    name: Optional[str]
    size: float
    type: str
    mime_type: str
    content: str


class ResponseImage(BaseModel):
    name: Optional[str]
    url: Optional[str]


class RequestPublication(BaseModel):
    title: str
    body: str
    images: Optional[str]
    tags: str
    author: Optional[Author]
    date_of_publication: Optional[str]
    status: Optional[bool] = True


class ResponsePublication(BaseModel):
    uuid: str
    title: str
    body: str
    images: Optional[str]
    tags: List[str]
    author: Optional[Author]
    date_of_publication: Optional[str]
    status: Optional[bool]


class ResponseUpdateOrDelete(BaseModel):
    uuid: str
