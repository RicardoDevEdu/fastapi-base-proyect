from fastapi import APIRouter


router = APIRouter()


@router.post(
    "/auth/login",
    tags=['Service Auth']
)
def login(id):
    return {'id': id}

