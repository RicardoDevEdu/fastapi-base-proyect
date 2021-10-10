from app.core.exceptions import BusinessException


class MaterialNotFound(BusinessException):

    def __init__(self, message: str):
        self.message = f"User with uuid: {message} not exists"

    code_error = "USER-1002"
    status_code = 404
