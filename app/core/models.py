import os
from datetime import datetime
from uuid import uuid4
from mongoengine import (
    fields,
    DynamicDocument,
    EmbeddedDocumentField
)


class DocumentBase:
    meta = {'db_alias': os.getenv("MONGO_NAME")}
    created_at = fields.DateTimeField(
        default=datetime.now(),
    )
    updated_at = fields.DateTimeField(
        default=datetime.now(),
        null=True
    )


class User(DynamicDocument, DocumentBase):
    uuid = fields.UUIDField(default=uuid4())
    name = fields.StringField(max_length=160, required=True)
    last_name = fields.StringField(max_length=160, required=True)
    email = fields.StringField(max_length=160, required=True)
    password = fields.StringField(max_length=160, required=True)


