from app.core.applications.user.core.handlers import UserHandler
from app.core.applications.user.core.serializable import (
    RequestUserCompany, 
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
