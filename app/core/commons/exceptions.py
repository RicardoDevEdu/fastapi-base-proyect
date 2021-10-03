
from pydantic.main import BaseModel
from app.core.exceptions import BusinessException


class MongoUniqueError(BusinessException):

    def __init__(self, message: str):
        self.message = f"Attribute {message} already exists"

    code_error = "USER-1001"    
    status_code = 403


class ModelNotFound(BusinessException):

    def __init__(self,model: BaseModel, uuid: str):
        self.message = f"{model.__name__} with uuid: {uuid} not exists"

    code_error = "MODEL-1002"
    status_code = 404
