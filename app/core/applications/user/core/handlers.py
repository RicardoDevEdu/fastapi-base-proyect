import json
from app.core.applications.user.core.services.userservice import UserService
from app.core.applications.user.core.serializable import RequestUserCompany


class UserHandler:

    @staticmethod
    def create_company(data: RequestUserCompany):
        user_sevice = UserService()
        comapny = user_sevice.create_company(data)
     
        return json.loads(comapny.to_json())