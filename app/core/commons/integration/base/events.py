from abc import ABC
from app.core.commons.integration.base.subscribers import SUBSCRIBER
import importlib


class BaseEvent(ABC):
    pass


class EventHandler:

    event: BaseEvent

    def __init__(self, event: BaseEvent) -> None:
        self.event = event
        self.event_class_name = self.event.__class__.__name__
        self.event_module_path = self.event.__module__

    def emmit(self):
        self._find_listener()

    def _find_listener(self):
        app_name = self._get_application_name()
        listener_module = f'app.core.commons.integration.{app_name}.listeners'
        module = importlib.import_module(listener_module)
        self._run_instance(module)

    def _run_instance(self, module):
        listeners = SUBSCRIBER.get(self.event_class_name)
        for listener in listeners:
            iinstance = getattr(module, listener)
            iinstance.handler(self, self.event)

    def _get_application_name(self):
        path = self.event_module_path.split('.')
        return path[-2]
