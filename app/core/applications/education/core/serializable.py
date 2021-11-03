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
    images: Optional[str]
    features: str
    pull_apart: str 
    process: str


class ResponseMaterial(BaseModel):
    uuid: str
    tag: str
    name: str
    images: Optional[str]
    features: str
    pull_apart: str 
    process: str


class ResponseUpdateOrDelete(BaseModel):
    uuid: str
