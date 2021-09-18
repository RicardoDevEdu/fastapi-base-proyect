import json
from app.core.applications.auth.core.models import Auth
from app.core.QuerySet import GenericQuerySet
from app.core.applications.auth.core.services.Oauth2 import Oauth2Service
from app.core.applications.auth.core.serializable import RequestLogin


class AuthHandler:

    @staticmethod
    def login(data: RequestLogin):
        oauth2Service = Oauth2Service(data)
        auth = oauth2Service.authenticate()
        token = oauth2Service.create_access_token()
        return {
            "data": json.loads(auth.to_json()),
            "access_token": token,
            "token_type": "bearer"
        }

    @staticmethod
    def current_auth(token: str):
        auth = Oauth2Service.get_current_auth(token)
        return json.loads(auth.to_json())
