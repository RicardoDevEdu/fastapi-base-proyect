from typing import List, Optional

from fastapi.params import Query
from app.core.applications.user.core.handlers import UserHandler
from app.core.applications.user.core.serializable import (
    RequestUpdateUser,
    RequestUserCompany,
    RequestUser,
    ResponseUpdateOrDelete,
    ResponseUser,
    ResponseUserCompany,
    RequestUserFolow
)
from fastapi import APIRouter


router = APIRouter()


@router.post(
    "/user/company",
    response_model=ResponseUserCompany,
    tags=['Company']
)
def register(form_data: RequestUserCompany):
    return UserHandler.create_company(form_data.dict())


@router.get(
    "/user/company",
    response_model=List[ResponseUserCompany],
    tags=['Company']
)
def list_companies(tags: List[str] = Query(None)):
    return UserHandler.list_company()


@router.get(
    "/user/company/extra",
    response_model=ResponseUserCompany,
    tags=['Company']
)
def get_company_extra(uuid: str, name: str):
    return UserHandler.get_company_extra(uuid, name)


@router.get(
    "/user/company/{uuid}",
    response_model=ResponseUserCompany,
    tags=['Company']
)
def get_company(uuid: str):
    return UserHandler.get_company(uuid)





@router.patch(
    "/user/{uuid_user}/folow",
    response_model=ResponseUpdateOrDelete,
    tags=['User Actions and Special Filters']
)
def folow(uuid_user: str, form_data: RequestUserFolow):
    return UserHandler.folow(uuid_user, form_data.dict())


@router.get(
    "/user/company/geolocation",
    response_model=List[ResponseUserCompany],
    tags=['User Actions and Special Filters']
)
def geolocation(lat: float, long: float, max_distance: int = 1000, tags: List[str] = Query(None)):
    return UserHandler.geolocation(lat, long, max_distance, tags)


@router.post(
    "/user/producer",
    response_model=ResponseUser,
    tags=['User']
)
def register_produccer(form_data: RequestUser):
    data = form_data.dict()
    data['roles'] = ['producer']
    return UserHandler.create_user(data)


@router.post(
    "/user",
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
    tags=['User'],
    summary="Create system user"
)
def list(q: Optional[str] = None, roles: List[str] = Query(None), status: bool = True):
    return UserHandler.list(roles, status)


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
