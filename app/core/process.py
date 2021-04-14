from app.v1.helpers import meta_paginate
from app.core.QuerySet import GenericQuerySet
import json

from mongoengine.queryset.visitor import Q
from .models import User
from pydantic.types import List




class ServicesProcess:
    def __init__(self):
        pass


    def init(self):

        user = User(
           name ="retet",
           last_name="erter",
           email="erter",
           password="sadasd",
           address=[
               {
                   "name":"w"
               }, 
               {
                   "name":"e"
               }
           ] 
        ).save()

        return user
    
    def find(self, params: dict):
        userQuerySet = GenericQuerySet(User)    
        paginate = meta_paginate({"name":'retet'}, params, userQuerySet)
        return paginate;
