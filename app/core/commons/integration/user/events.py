from app.core.commons.integration.base.events import BaseEvent
from app.core.applications.user.core.models import (
    Company,
    User
)

class RegisterUserCompanyEvent(BaseEvent):
    def __init__(self, company: Company):
        self.company = company


class RegisterUserEvent(BaseEvent):
    def __init__(self, user: User):
        self.user = user