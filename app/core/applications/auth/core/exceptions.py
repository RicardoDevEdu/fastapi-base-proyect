

from app.core.exceptions import BusinessException

class CredentialInvalid(BusinessException):
    code_error = "AUTH-1001"
    message = "Could not validate credentials"
    status_code = 401

class InactiveUser(BusinessException):
    code_error = "AUTH-1002"
    message = "Inactive user"


