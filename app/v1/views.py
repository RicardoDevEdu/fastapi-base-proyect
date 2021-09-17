from typing import List
from fastapi.encoders import jsonable_encoder
from .serializers import BasePaginate, User, UserPaginate
from fastapi import APIRouter, Response
from fastapi.params import Query
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.core.handlers import SignProcessHandler
from app.core.helpers import notify_sns


router = APIRouter()


@router.get(
    "/info/",
    tags=['User']
)
def cancel():
    return JSONResponse(status_code=200, content=jsonable_encoder(SignProcessHandler.init()))


@router.get(
    "/find/",
    response_model=UserPaginate,
    tags=['User']
)
def find(item_per_page: int = 15, page: int = 1, order: str = "ASC", model_uuid: str = None):
    params = {
        "item_per_page": item_per_page,
        "page": page,
        "order": order,
        "model_uuid": model_uuid
    }
    return SignProcessHandler.find(params)
