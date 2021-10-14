from abc import ABC
from datetime import datetime
from typing import Optional

from mongoengine.errors import NotUniqueError
from pydantic.main import BaseModel
from app.core.commons.QuerySet import GenericQuerySet

from app.core.commons.exceptions import ModelNotFound, MongoUniqueError
from app.core.commons.helpers import remove_item_none_of_dict


class GenericService(ABC):

    def __init__(self, model: BaseModel):
        self.model = model
        self.querySet = GenericQuerySet(self.model)

    def set_query_set(self, model: BaseModel):
        self.querySet = GenericQuerySet(model)

    @property
    def query_set(self):
        return self.querySet

    def create(self, data: BaseModel):
        querySet = self.querySet
        try:
            return querySet.create(dict(data))
        except NotUniqueError:
            raise MongoUniqueError("")

    def list(self, q: Optional[str] = None):
        querySet = self.querySet

        query_filter = dict(
            status=True,
            deleted_at=None    
        )     

        models = querySet.all(query_filter)

        if q is not None:
            models = models.search_text(q)

        return models

    def update(self, id: str, data):
        try:
            querySet = self.querySet
            querySet.update(
                dict(uuid=id),
                remove_item_none_of_dict(data)
            )
            return id
        except NotUniqueError:
            raise MongoUniqueError("")

    def delete(self, id: str):
        querySet = self.querySet
        querySet.update_key('deleted_at', datetime.now(), id)
        return id

    def get(self, id: str):
        querySet = self.querySet

        model = querySet.filter_one(dict(
            uuid=id,
            deleted_at=None
        ))

        if model is None:
            raise ModelNotFound(self.model, id)

        return model
