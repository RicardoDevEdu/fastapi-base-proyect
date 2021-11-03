from pydantic.main import BaseModel


class ImagenData(BaseModel):
    type: str
    mimetype: str
    encode: str
    content: str