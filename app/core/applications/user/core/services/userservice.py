from datetime import datetime
from app.core.applications.user.core.exceptions import MongoUniqueError, UserNotFound
from typing import Dict, List

from mongoengine.errors import NotUniqueError
from app.core.applications.user.core.models import Company, User
from app.core.applications.auth.core.QuerySet import GenericQuerySet
from app.core.applications.user.core.serializable import (
    RequestUpdateUser,
    RequestUser,
    RequestUserCompany
)
from passlib.context import CryptContext

from app.core.helpers import remove_item_none_of_dict


class UserService:
    def __init__(self):
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def create_company(self, data: RequestUserCompany) -> Company:
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

    def create(self, data: RequestUser) -> User:
        model_user = GenericQuerySet(User)
        try:
            data.update({
                "auth": {
                    "hashed_password": self._pwd_context.hash(data.get('auth').get('hashed_password'))
                }
            })
            user = model_user.create(dict(data))

            return user
        except NotUniqueError:
            raise MongoUniqueError("email, identification or name")

    def list(self) -> List[User]:
        model_user = GenericQuerySet(User)

        users = model_user.all(dict(
            status=True,
            deleted_at=None
        ))
        return users

    def update(self, id: str, data: RequestUpdateUser) -> User:
        try:
            model_user = GenericQuerySet(User)

            data.update({
                "auth": {
                    "hashed_password": self._pwd_context.hash(data.get('auth').get('hashed_password'))
                }
            })

            model_user.update(
                dict(uuid=id),
                remove_item_none_of_dict(data)
            )
            return id
        except NotUniqueError:
            raise MongoUniqueError("email")

    def delete(self, id: str):
        model_user = GenericQuerySet(User)
        model_user.update_key('deleted_at', datetime.now(), id)
        return id

    def get(self, id: str) -> User:
        model_user = GenericQuerySet(User)

        users = model_user.filter_one(dict(
            uuid=id,
            deleted_at=None
        ))

        if users is None:
            raise UserNotFound(id)

        return users
