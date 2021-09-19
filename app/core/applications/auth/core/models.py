import os
from datetime import datetime
from uuid import uuid4
from mongoengine import (
    fields
)
from mongoengine.document import DynamicDocument


class DocumentBase():
    meta = {'db_alias': os.environ.get("MONGO_NAME")}
    created_at = fields.DateTimeField(
        default=datetime.now(),
    )
    updated_at = fields.DateTimeField(
        default=datetime.now(),
        null=True
    )


class Auth(DynamicDocument, DocumentBase):
    uuid = fields.UUIDField(default=uuid4(), binary=False)
    full_name = fields.StringField(max_length=160, required=True, default=None)
    email = fields.StringField(max_length=160, required=True)
    hashed_password = fields.StringField(max_length=160, required=True)
    disabled = fields.BooleanField(default=False)
