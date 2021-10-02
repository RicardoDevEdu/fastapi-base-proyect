from app.core.commons.integration.user.events import RegisterUserCompanyEvent
from app.core.commons.integration.base.events import EventHandler
import json
from app.core.applications.user.core.services.userservice import UserService
from app.core.applications.user.core.serializable import RequestUserCompany


class UserHandler:

    @staticmethod
    def create_company(data: RequestUserCompany):
        user_sevice = UserService()
        company = user_sevice.create_company(data)

        """
        Emmit event register compay
        """
        EventHandler(RegisterUserCompanyEvent(company)).emmit()
     
        return json.loads(company.to_json())