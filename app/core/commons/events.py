from app.core.commons.listeners.register_user import RegisterUser
from typing import List
from app.core.applications.auth.core.models import Auth
from app.core.commons.subscribers import SUBSCRIBER
from abc import ABC
import importlib

class BaseEvent(ABC):
    pass

class Event:

    event: BaseEvent
    RegisterUser
    def __init__(self, event: BaseEvent) -> None:
        self.event = event
    
    def emmit(self):
        self._find_listener()

    def _find_listener(self):
        class_name = self.event.__class__.__name__
        listener_module = f'app.core.commons.listeners.register_user'      
        module = importlib.import_module(listener_module)            

        listeners = SUBSCRIBER.get(class_name)
        for listener in listeners:
            iinstance = getattr(module, listener)
            iinstance.handler(self, self.event)
            
        return listeners
    
    def inject(event: str, listeners: List[str]):
        pass

class RegisterAuth(BaseEvent):
    def __init__(self, auth: Auth):
        self.name = "Este es el evento de register auth"
        self.auth = auth