import json
import os
import requests
from typing import List
from app.core.applications.user.core.models import Company
from app.core.applications.user.core.serializable import (
    RequestUpdateUser,
    RequestUser,
    RequestUserCompany
)
from app.core.commons.services.genericservice import GenericService


class ExtraService(GenericService):
    def __init__(self):
        super().__init__(Company)

    def get_extra_data(self, uuid:str,  name:str):

        rues_data = self.rues(name)

        if rues_data is None:
            return rues_data

        data = {
            "third_party_data" :self.rues(name)
        } 
        self.update(uuid, data)
       
        return self.get(uuid)

    def rues(self, name: str):
        url = os.getenv('HOST_MISTADOS_RUES')
        token = os.getenv('TOKEN_MISTADOS_RUES')
        headers = {'Authorization': token}

        response = requests.post(url, 
        data=dict(
            razonSocial=name
        ),
        headers=headers
        )

        response = response.json()

        if response.get('data'):
            return response.get('data')[0]

        return None
