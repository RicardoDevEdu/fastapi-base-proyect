import json
import pydash as _
from typing import Any, Union, Dict, List, Optional

ExceptionMessageType = Union[str, Dict[str, Any], List[Dict[str, Any]]]


class BusinessException(Exception):
    """Excepción de negocio."""
    code_error = 1001
    message: ExceptionMessageType
    status_code: Optional[int]

    def __init__(self,
                 message: ExceptionMessageType = None,
                 code_error: int = None,
                 status_code: int = None,
                 *args):
        if not _.is_empty(message):
            self.message = json.loads(
                message) if _.is_json(message) else message
        if code_error is not None:
            self.code_error = code_error
        if status_code is not None:
            self.status_code = status_code

        super().__init__(self.message, *args)


class FailedLoadEnv(BusinessException):
    code_error = "CONFIG-2001"
    message = "Failied loading environment"
