from typing import List
from app.core.applications.user.core.handlers import UserHandler
from app.core.applications.user.core.serializable import (
    RequestUpdateUser,
    RequestUserCompany,
    RequestUser,
    ResponseUpdateOrDelete,
    ResponseUser,
    ResponseUserCompany
)
from fastapi import APIRouter


router = APIRouter()


@router.post(
    "/user/company",
    response_model=ResponseUserCompany,
    tags=['User']
)
def register(form_data: RequestUserCompany):
    return UserHandler.create_company(form_data.dict())


@router.post(
    "/user/producer",
    response_model=ResponseUser,
    tags=['User']
)
def register_produccer(form_data: RequestUser):
    return UserHandler.create_user(form_data.dict())


@router.put(
    "/user/{uuid}",
    response_model=ResponseUpdateOrDelete,
    tags=['User']
)
def update(uuid: str, form_data: RequestUpdateUser):
    return UserHandler.update(uuid, form_data.dict())


@router.get(
    "/user",
    response_model=List[ResponseUser],
    tags=['User']
)
def list():
    return UserHandler.list()


@router.delete(
    "/user/{uuid}",
    response_model=ResponseUpdateOrDelete,
    tags=['User']
)
def delete(uuid: str):
    return UserHandler.delete(uuid)


@router.get(
    "/user/{uuid}",
    response_model=ResponseUser,
    tags=['User']
)
def get(uuid: str):
    return UserHandler.get(uuid)
