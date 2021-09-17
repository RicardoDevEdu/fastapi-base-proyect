from fastapi import APIRouter


router = APIRouter()


@router.get(
    "/user/{id}",
    tags=['Service User']
)
def get(id):
    return {'id': id}

