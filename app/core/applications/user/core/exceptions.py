from app.core.exceptions import BusinessException


class UserNotFound(BusinessException):

    def __init__(self, message: str):
        self.message = f"User with uuid: {message} not exists"

    code_error = "USER-1002"
    status_code = 404


class ExtradataNotFound(BusinessException):

    def __init__(self):
        self.message = f"Extra data not found"

    code_error = "COMPANY-1004"
    status_code = 404

