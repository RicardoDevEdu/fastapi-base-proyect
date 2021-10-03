from enum import unique
import os
from datetime import datetime
from uuid import uuid4
from mongoengine import (
    fields
)
from mongoengine.document import DynamicDocument


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


class Company(DynamicDocument, DocumentBase):
    uuid = fields.UUIDField(default=uuid4(), binary=False)    
    email = fields.StringField(max_length=160, required=True, unique=True)
    idetitification_type: fields.StringField(max_length=5, required=True, default=None)
    number_identification: fields.StringField(max_length=16, required=True, default=None, unique=True)
    business_name: fields.StringField(max_length=160, required=True, default=None, unique=True)
    address: fields.StringField(max_length=160, required=True, default=None)
    location: fields.DictField()
    status: fields.BooleanField(default=False, required=False)
    disabled = fields.BooleanField(default=False, required=False)
    auth: fields.DictField()

class User(DynamicDocument, DocumentBase):
    uuid = fields.UUIDField(default=uuid4(), binary=False)    
    email = fields.StringField(max_length=160, required=True, unique=True)
    idetitification_type: fields.StringField(max_length=5, required=False, default=None)
    number_identification: fields.StringField(max_length=16, required=False, default=None, unique=True)
    name: fields.StringField(max_length=160, required=False, default=None, unique=True)
    last_name: fields.StringField(max_length=160, required=False, default=None, unique=True)
    address: fields.StringField(max_length=160, required=True, default=None)
    status: fields.BooleanField(default=False, required=False)
    disabled = fields.BooleanField(default=False, required=False)
    auth: fields.DictField()
    scope: fields.DictField(required=False, default={})
