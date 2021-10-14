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


class Feature(EmbeddedDocument):
    text = fields.StringField(max_length=160, required=True)


class PullApart(EmbeddedDocument):
    text = fields.StringField(max_length=160, required=True)


class Gather(EmbeddedDocument):
    text = fields.StringField(max_length=160, required=True)


class Process(EmbeddedDocument):
    text = fields.StringField(max_length=160, required=True)


class Image(EmbeddedDocument):
    name = fields.StringField(max_length=160, required=False, unique=True)
    size = fields.FloatField(required=False)
    url = fields.StringField(max_length=200, required=True, unique=True)


class Material(DynamicDocument, DocumentBase):
    uuid = fields.UUIDField(default=uuid4(), binary=False)
    tag = fields.StringField(max_length=160, required=True, unique=True)
    name = fields.StringField(max_length=160, required=True, unique=True)
    description = fields.StringField(max_length=500, required=True, unique=True)
    image = fields.EmbeddedDocumentField(Image)
    features = fields.ListField(fields.EmbeddedDocumentField(Feature), required=False)
    pull_apart = fields.ListField(fields.EmbeddedDocumentField(PullApart), required=False)
    gather = fields.ListField(fields.EmbeddedDocumentField(Gather), required=False)
    process = fields.ListField(fields.EmbeddedDocumentField(Process), required=False)
    status= fields.BooleanField(default=True, required=False)

    meta = {'indexes': [
        {'fields': ['$name', "$description"],
         'default_language': 'spanish',
         'weights': {'description': 10, 'name': 2}
        }
    ]}