from app.core.exceptions import BusinessException


class MongoUniqueError(BusinessException):

    def __init__(self, message: str):
        self.message = f"Attribute {message} already exists"

    code_error = "USER-1001"    
    status_code = 403


class UserNotFound(BusinessException):

    def __init__(self, message: str):
        self.message = f"User with uuid: {message} not exists"

    code_error = "USER-1002"    
    status_code = 404