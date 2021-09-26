from app.core.applications.user.core.exceptions import MongoUniqueError
from typing import Dict

from mongoengine.errors import NotUniqueError
from app.core.applications.user.core.models import Company
from app.core.applications.auth.core.QuerySet import GenericQuerySet
from app.core.applications.user.core.serializable import RequestUserCompany
from passlib.context import CryptContext


class UserService:
    def __init__(self):
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def create_company(self, data: RequestUserCompany):
        model_company = GenericQuerySet(Company)
        try:
            data.update({
                "auth": {
                    "hashed_password": self._pwd_context.hash(data.get('auth').get('hashed_password'))
                }
            })
            company = model_company.create(dict(data))
            return company
        except NotUniqueError:
            raise MongoUniqueError("email, identification or name")
