from typing import List
from app.core.applications.publication.core.handlers import PublicationHandler
from app.core.applications.publication.core.serializable import (
 RequestPublication,
 ResponsePublication,
 ResponseUpdateOrDelete
)
from fastapi import APIRouter


router = APIRouter()



@router.post(
    "/publication",
    response_model=ResponsePublication,
    tags=['Publications']
)
def create(form_data: RequestPublication):
    return PublicationHandler.create(form_data.dict())


@router.put(
    "/publication/{uuid}",
    response_model=ResponseUpdateOrDelete,
    tags=['Publications']
)
def update(uuid: str, form_data: RequestPublication):
    return PublicationHandler.update(uuid, form_data.dict())


@router.get(
    "/publication",
    response_model=List[ResponsePublication],
    tags=['Publications']
)
def list():
    return PublicationHandler.list()


@router.delete(
    "/publication/{uuid}",
    response_model=ResponseUpdateOrDelete,
    tags=['Publications']
)
def delete(uuid: str):
    return PublicationHandler.delete(uuid)


@router.get(
    "/publication/{uuid}",
    response_model=ResponsePublication,
    tags=['Publications']
)
def get(uuid: str):
    return PublicationHandler.get(uuid)
