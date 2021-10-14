from enum import unique
import os
from datetime import datetime
from uuid import uuid4
from mongoengine import (
    fields
)
from mongoengine.document import DynamicDocument, EmbeddedDocument


class DocumentBase:
    meta = {'db_alias': os.environ.get("MONGO_NAME")}
    created_at = fields.DateTimeField(
        default=datetime.now(),
    )
    updated_at = fields.DateTimeField(
        default=datetime.now(),
        null=True
    )
    deleted_at = fields.DateTimeField(
        default=datetime.now(),
        null=True
    )

class Author(EmbeddedDocument):
    name: fields.StringField(max_length=160, required=True, unique=True)
    mode: fields.StringField(max_length=160, required=True, unique=True)
    uuid: fields.StringField(max_length=160, required=True, unique=True)


class Image(EmbeddedDocument):
    name: fields.StringField(max_length=160, required=False, unique=True)
    size: fields.FloatField(required=False)
    url: fields.StringField(max_length=200, required=True, unique=True)


class Publication(DynamicDocument, DocumentBase):
    uuid = fields.UUIDField(default=uuid4(), binary=False)
    title: fields.StringField(max_length=160, required=True, unique=True)
    body: fields.StringField(max_length=500, required=True, unique=True)
    images: fields.ListField(fields.EmbeddedDocumentField(Image))
    tags: fields.ListField(fields.StringField())
    author: fields.EmbeddedDocumentField(Author)
    date_of_publication: fields.StringField(max_length=160, required=True, unique=True)
    status: fields.BooleanField(default=True, required=False)
