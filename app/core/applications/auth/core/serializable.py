from typing import List, Optional

from pydantic.main import BaseModel


class RequestLogin(BaseModel):
    grant_type: str = "password"
    email: str
    password: str
    scope: str = ""
    client_id: Optional[str] = None
    client_secret: Optional[str] = None


class ResponseAuth(BaseModel):
    uuid: str
    full_name: str
    email: str
    disabled: bool


class ResponseTokenAut(BaseModel):
    data: ResponseAuth
    access_token: str
    token_type: str


class Auth(BaseModel):
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = False
    hashed_password: str


class RequestAuth(BaseModel):
    email: str
    hashed_password: str
    full_name: Optional[str]
    disabled: Optional[bool]    
    roles: Optional[List[str]]
    scopes: Optional[List[str]]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
