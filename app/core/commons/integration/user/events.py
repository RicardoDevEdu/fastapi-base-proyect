from app.core.commons.integration.base.events import BaseEvent
from app.core.applications.user.core.models import Company

class RegisterUserCompanyEvent(BaseEvent):
    def __init__(self, company: Company):
        self.company = company