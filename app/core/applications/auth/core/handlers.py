
from app.core.commons.integration.auth.events import RegisterAuth
from app.core.commons.integration.base.events import EventHandler
import json
from app.core.applications.auth.core.services.Oauth2 import Oauth2Service
from app.core.applications.auth.core.serializable import RequestAuth, RequestLogin


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
    def register(data: RequestAuth, hash_password: bool = True):
        auth = Oauth2Service.register(data, hash_password)
        
        """
        send event
        """ 
        EventHandler(RegisterAuth(auth)).emmit()
         
        return json.loads(auth.to_json())

    @staticmethod
    def current_auth(token: str):
        auth = Oauth2Service.get_current_auth(token)
        return json.loads(auth.to_json())
