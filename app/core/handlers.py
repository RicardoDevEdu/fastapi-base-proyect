import json
from uuid import UUID
from datetime import datetime
from littlenv import littlenv
from app.core import exceptions
from app.core.process import ServicesProcess
from app.core.models import Rule


littlenv.load()


class SignProcessHandler:

    @staticmethod
    def init():     
        service = ServicesProcess()
        return service.init()
