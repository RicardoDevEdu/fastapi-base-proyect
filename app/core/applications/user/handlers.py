import json
from uuid import UUID
from datetime import datetime
from littlenv import littlenv
from app.core import exceptions
from app.core.process import ServicesProcess


# littlenv.load()


class SignProcessHandler:

    @staticmethod
    def init():
        service = ServicesProcess()
        return service.init()

    @staticmethod
    def find(params: dict):
        service = ServicesProcess()
        return service.find(params)
