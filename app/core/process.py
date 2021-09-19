from app.v1.helpers import meta_paginate
from app.core.QuerySet import GenericQuerySet
from .models import User


class ServicesProcess:
    def __init__(self):
        pass

    def init(self):

        user = User(
            name="retet",
            last_name="erter",
            email="erter",
            password="sadasd",
            address=[
                {
                    "name": "w"
                },
                {
                    "name": "e"
                }
            ]
        ).save()

        return user

    def find(self, params: dict):
        userQuerySet = GenericQuerySet(User)
        paginate = meta_paginate({"name": 'retet'}, params, userQuerySet)
        return paginate
