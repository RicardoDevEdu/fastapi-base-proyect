from typing import Optional
from pydantic.main import BaseModel


class Location(BaseModel):
    latitud: float
    longitud: float


class ThirdPartyData(BaseModel):
    categoria_matricula: str
    clase_identificacion: Optional[str]
    codigo_camara: int
    codigo_estado: str
    identificacion: Optional[str]
    estado: str
    numero_matricula: str
    nombre_camara: str
    organizacion_juridica: str
    razon_social: str
    sigla: Optional[str]
    tipo_empresa: str


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
    third_party_data: Optional[ThirdPartyData]


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


class ResponseUpdateOrDelete(BaseModel):
    uuid: str
