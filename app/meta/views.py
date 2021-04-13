from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse
from config.settings.base import API_VERSION, APP_DESCRIPTION
router = APIRouter()


@router.get("/", tags=["meta"])
async def root():
    return {"Service":APP_DESCRIPTION}


@router.get("/version", tags=["meta"])
async def version():
    response = {
        "version": API_VERSION,
        "message": APP_DESCRIPTION
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )


@router.get("/health", tags=["meta"])
async def health_check():
    response = {"satus": "ok"}
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )
