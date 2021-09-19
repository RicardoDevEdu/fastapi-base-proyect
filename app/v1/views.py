from .serializers import UserPaginate
from fastapi import APIRouter
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.core.handlers import SignProcessHandler


router = APIRouter()


@router.get(
    "/info/",
    tags=['Others']
)
def cancel():
    return JSONResponse(status_code=200, content=jsonable_encoder(SignProcessHandler.init()))


@router.get(
    "/find/",
    response_model=UserPaginate,
    tags=['Others']
)
def find(item_per_page: int = 15, page: int = 1, order: str = "ASC", model_uuid: str = None):
    params = {
        "item_per_page": item_per_page,
        "page": page,
        "order": order,
        "model_uuid": model_uuid
    }
    return SignProcessHandler.find(params)
