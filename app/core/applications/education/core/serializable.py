from typing import List, Optional
from pydantic.main import BaseModel


class Features(BaseModel):
    text: str


class PullApart(BaseModel):
    text: str


class Gather(BaseModel):
    text: str


class Process(BaseModel):
    text: str


class Image(BaseModel):
    name: Optional[str]
    size: float
    type: str
    mime_type: str
    content: str


class ResponseImage(BaseModel):
    name: Optional[str]
    url: Optional[str]


class RequestMaterial(BaseModel):
    tag: str
    name: str
    description: str
    image: Image
    features: Optional[List[Features]]
    pull_apart: Optional[List[PullApart]]
    gather: Optional[List[Gather]]
    process: Optional[List[Process]]


class ResponseMaterial(BaseModel):
    uuid: str
    tag: str
    name: str
    description: str
    image: ResponseImage
    features: Optional[List[Features]]
    pull_apart: Optional[List[PullApart]]
    gather: Optional[List[Gather]]
    process: Optional[List[Process]]


class ResponseUpdateOrDelete(BaseModel):
    uuid: str
