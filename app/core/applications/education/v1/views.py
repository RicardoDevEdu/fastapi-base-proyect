from typing import List, Optional
from app.core.applications.education.core.handlers import EducationHandler
from app.core.applications.education.core.serializable import (
 ResponseMaterial,
 RequestMaterial,
 ResponseUpdateOrDelete
)
from fastapi import APIRouter


router = APIRouter()



@router.post(
    "/material",
    response_model=ResponseMaterial,
    tags=['Materials']
)
def create(form_data: RequestMaterial):
    return EducationHandler.create(form_data.dict())


@router.put(
    "/material/{uuid}",
    response_model=ResponseUpdateOrDelete,
    tags=['Materials']
)
def update(uuid: str, form_data: RequestMaterial):
    return EducationHandler.update(uuid, form_data.dict())


@router.get(
    "/material",
    response_model=List[ResponseMaterial],
    tags=['Materials'],
    summary= "Listado de materiales y filtro por descripción"
)
def list(q: Optional[str] = None):
    return EducationHandler.list(q)


@router.delete(
    "/material/{uuid}",
    response_model=ResponseUpdateOrDelete,
    tags=['Materials']
)
def delete(uuid: str):
    return EducationHandler.delete(uuid)


@router.get(
    "/material/{uuid}",
    response_model=ResponseMaterial,
    tags=['Materials']
)
def get(uuid: str):
    return EducationHandler.get(uuid)
