import json

from mongoengine.queryset.visitor import Q
from pydantic.types import List




class ServicesProcess:
    def __init__(self):
        pass


    def init(self):
        return {
            "process_id": "",
            "documents": "",
            "created_at": ""
        }
