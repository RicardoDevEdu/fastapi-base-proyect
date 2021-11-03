from enum import Enum
from typing import List, Optional, Union
from pydantic.main import BaseModel


class Location(BaseModel):
    type: Optional[str] = "Point"
    coordinates: List[float]

class TypeModelEnum(str, Enum):
    user = 'user'
    company = 'company'

class RequestUserFolow(BaseModel):
    type: TypeModelEnum = TypeModelEnum.user
    name: str
    uuid: str

class ThirdPartyData(BaseModel):
    categoriaMatricula: str
    claseIdentificacion: Optional[str]
    codigoCamara: int
    codigoEstado: str
    identificacion: Optional[str]
    estado: str
    numeroMatricula: str
    nombreCamara: str
    organizacionJuridica: str
    razonSocial: str
    sigla: Optional[str]
    tipoEmpresa: str


class RequestAuthUser(BaseModel):
    hashed_password: str


class ApprovedBy(BaseModel):
    name: str
    date: str


class RequestUserCompany(BaseModel):
    idetitification_type: str
    number_identification: str
    email: str
    business_name: Optional[str]
    address: Optional[str]
    location: Optional[Location]
    status: bool
    tags: List[str]
    auth: RequestAuthUser


class ResponseUserCompany(BaseModel):
    uuid: str
    idetitification_type: str
    number_identification: str
    email: str
    business_name: Optional[str]
    address: Optional[str]
    location: Optional[Location]
    status:     bool
    approved_by: Optional[ApprovedBy]
    third_party_data: Optional[Union[ThirdPartyData,None]]


class RequestUser(BaseModel):
    email: str
    name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]
    status: Optional[bool] = True
    auth: RequestAuthUser
    scope: Optional[dict]


class RequestUpdateUser(BaseModel):
    email: Optional[str]
    name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]
    status: Optional[bool] = True
    auth: Optional[RequestAuthUser]
    scope: Optional[dict]


class ResponseUser(BaseModel):
    uuid: str
    email: str
    name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]
    status: Optional[bool] = True
    scope: Optional[dict]
    roles: Optional[List[str]]


class ResponseUpdateOrDelete(BaseModel):
    uuid: str
