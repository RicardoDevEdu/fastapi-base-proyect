from typing import List
from app.core.applications.user.core.exceptions import ExtradataNotFound
from app.core.applications.user.core.services.extraservice import ExtraService
from app.core.applications.user.core.services.geoservice import GeoService
from app.core.commons.integration.user.events import (
    RegisterUserCompanyEvent,
    RegisterUserEvent,
    UpdateUserEvent
)
from app.core.commons.integration.base.events import EventHandler
import json
from app.core.applications.user.core.services.userservice import UserService
from app.core.applications.user.core.serializable import (
    RequestUpdateUser,
    RequestUserCompany,
    RequestUser,
    RequestUserFolow
)


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

    @staticmethod
    def list_company():
        model_sevice = UserService()
        model = model_sevice.list_company_with_filter()
        return json.loads(model.to_json())

    @staticmethod
    def get_company(id: str):
        user_sevice = UserService()
        users = user_sevice.get_company(id)
        return json.loads(users.to_json())

    @staticmethod
    def geolocation(lat: float, long: float, max_distance: int, tags: List[str] = None):
        sevice = GeoService()
        models = sevice.location_near(lat, long, max_distance, tags)

        return json.loads(models.to_json())


    @staticmethod
    def folow(uuid_user: str, form_data: RequestUserFolow):
        sevice = UserService()
        
        return dict(uuid=sevice.folow(uuid_user, form_data))

    @staticmethod
    def create_user(data: RequestUser):
        user_sevice = UserService()
        user = user_sevice.create_user(data)

        """
        Emmit event register user (system an producer)
        """
        EventHandler(RegisterUserEvent(user)).emmit()

        return json.loads(user.to_json())

    @staticmethod
    def update(id: str, data: RequestUpdateUser):
        user_sevice = UserService()

        user = user_sevice.get(id)

        """
        Emmit event update user
        """
        EventHandler(UpdateUserEvent(user)).emmit()

        return dict(uuid=user_sevice.update_user(id, data))

    @staticmethod
    def list(roles: List[str], status: bool = True):
        user_sevice = UserService()
        users = user_sevice.list_with_filter(roles=roles, status=status)
        return json.loads(users.to_json())

    @staticmethod
    def delete(id: str):
        user_sevice = UserService()
        return dict(uuid=user_sevice.delete(id))

    @staticmethod
    def get(id: str):
        user_sevice = UserService()
        users = user_sevice.get(id)
        return json.loads(users.to_json())


    @staticmethod
    def get_company_extra(uuid: str, name: str):
        service = ExtraService()
        model = service.get_extra_data(uuid, name)
        if model is None:
            raise ExtradataNotFound
        return json.loads(model.to_json())
