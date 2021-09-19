from app.core.commons.integration.base.events import BaseEvent
from app.core.applications.auth.core.models import Auth

class RegisterAuth(BaseEvent):
    def __init__(self, auth: Auth):
        self.name = "Este es el evento de register auth"
        self.auth = auth