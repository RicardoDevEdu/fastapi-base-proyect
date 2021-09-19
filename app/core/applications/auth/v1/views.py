from app.core.applications.auth.core.serializable import RequestLogin, ResponseAuth, ResponseTokenAut
from app.core.applications.auth.core.handlers import AuthHandler
from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post(
    "/auth/login",
    response_model=ResponseTokenAut,
    tags=['Service Auth']
)
def login(form_data: RequestLogin):
    return AuthHandler.login(form_data)


@router.get("/auth/me/", response_model=ResponseAuth)
def read_users_me(token: str = Depends(oauth2_scheme)):
    return AuthHandler.current_auth(token)
