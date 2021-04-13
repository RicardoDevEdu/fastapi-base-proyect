from fastapi import APIRouter, Response
from fastapi.params import Query
from starlette.responses import JSONResponse

from app.core.handlers import SignProcessHandler
from app.core.helpers import notify_sns



router = APIRouter()


@router.get(
    "/info/",
    response_class=JSONResponse,
    tags=['Sign process']
)
def cancel():
    return SignProcessHandler.init()

