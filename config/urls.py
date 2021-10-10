from fastapi import APIRouter
from app.meta import views as meta
from app.v1 import views as api_v1
from app.core.applications.user.v1 import views as api_user_v1
from app.core.applications.auth.v1 import views as api_auth_v1
from app.core.applications.publication.v1 import views as api_publication_v1

urls = APIRouter()

urls.include_router(
    meta.router,
    prefix=""
)

urls.include_router(
    api_v1.router,
    prefix="/api/v1"
)

urls.include_router(
    api_user_v1.router,
    prefix="/api/v1"
)

urls.include_router(
    api_auth_v1.router,
    prefix="/api/v1"
)


urls.include_router(
    api_publication_v1.router,
    prefix="/api/v1"
)
