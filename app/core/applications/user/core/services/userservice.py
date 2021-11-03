from typing import List
from app.core.applications.user.core.models import Company, User
from app.core.applications.user.core.serializable import (
    RequestUpdateUser,
    RequestUser,
    RequestUserCompany,
    RequestUserFolow
)
from passlib.context import CryptContext
from app.core.commons.services.genericservice import GenericService


class UserService(GenericService):
    def __init__(self):
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        super().__init__(User)

    def create_company(self, data: RequestUserCompany) -> Company:
        self.set_query_set(Company)
        data.update({
            "auth": {
                "hashed_password": self._pwd_context.hash(data.get('auth').get('hashed_password'))
            }
        })
        return self.create(data)

    def create_user(self, data: RequestUser) -> User:
        data.update({
            "auth": {
                "hashed_password": self._pwd_context.hash(data.get('auth').get('hashed_password'))
            }
        })
        return self.create(data)

    def update_user(self, id: str, data: RequestUpdateUser) -> User:

        if data.get('auth'):
            data.update({
                "auth": {
                    "hashed_password": self._pwd_context.hash(data.get('auth').get('hashed_password'))
                }
            })
        return self.update(id, data)

    def folow(self, uuid_user: str,  data: RequestUserFolow) -> str:
        self.set_query_set(User)
        self.model.objects(uuid=uuid_user).update_one(
            add_to_set__companies_followed=dict(
                uuid=data.get('uuid'),
                name=data.get('name'),
            )
        )
        return uuid_user

    def get_company(self, uuid: str):
        self.set_query_set(Company)
        return self.get(uuid)

    def list_with_filter(self, roles: List[str], status: bool = True):
        self.set_query_set(User)
        models = self.query_set.model.objects(
            deleted_at=None,
            __raw__={'roles': {'$in':roles}}
        )
        return models

    def list_company_with_filter(self, status: bool = True):
        self.set_query_set(Company)
        models = self.query_set.model.objects(
            deleted_at=None
        )
        return models
