
import os
import uuid
from enum import unique
from datetime import datetime
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

class CompaniesFollowed(EmbeddedDocument):
    uuid = fields.StringField(max_length=160, required=True, unique=True)
    name = fields.StringField(max_length=160, required=True, unique=True)


class CompanyExtraData(EmbeddedDocument):
    categoriaMatricula = fields.StringField(max_length=160, required=False, unique=False)
    claseIdentificacion = fields.StringField(max_length=160, required=False, unique=False)
    codigoCamara = fields.StringField(max_length=160, required=False, unique=False)
    codigoEstado = fields.StringField(max_length=160, required=False, unique=False)
    identificacion = fields.StringField(max_length=160, required=False, unique=False)
    estado = fields.StringField(max_length=160, required=False, unique=False)
    numeroMatricula = fields.StringField(max_length=160, required=False, unique=False)
    nombreCamara = fields.StringField(max_length=160, required=False, unique=False)
    organizacionJuridica = fields.StringField(max_length=160, required=False, unique=False)
    razonSocial = fields.StringField(max_length=160, required=False, unique=False)
    sigla = fields.StringField(max_length=160, required=False, unique=False)
    tipoEmpresa = fields.StringField(max_length=160, required=False, unique=False)

class Company(DynamicDocument, DocumentBase):
    uuid = fields.UUIDField(default=uuid.uuid4, binary=False, unique=True)    
    email = fields.StringField(max_length=160, required=True, unique=False)
    idetitification_type = fields.StringField(max_length=5, required=True, default=None)
    number_identification = fields.StringField(max_length=16, required=True, default=None, unique=True)
    business_name = fields.StringField(max_length=160, required=True, default=None, unique=True)
    address = fields.StringField(max_length=160, required=True, default=None)
    location = fields.PointField(auto_index=False)
    status = fields.BooleanField(default=False, required=False)
    disabled = fields.BooleanField(default=False, required=False)
    auth = fields.DictField()
    tags = fields.ListField(fields.StringField(), required=False, default=[])
    companies_followed = fields.ListField(CompaniesFollowed, required=False, default=[])
    third_party_data = fields.DictField(required=False, unique=False, default=None)

    meta = {
         'indexes': [[("location", "2dsphere")]]
    }

class User(DynamicDocument, DocumentBase):
    uuid = fields.UUIDField(default=uuid.uuid4, binary=False , unique=True)    
    email = fields.StringField(max_length=160, required=True, unique=False)
    idetitification_type = fields.StringField(max_length=5, required=False, default=None)
    number_identification = fields.StringField(max_length=16, required=False, default=None)
    name = fields.StringField(max_length=160, required=False, default=None)
    last_name = fields.StringField(max_length=160, required=False, default=None)
    address = fields.StringField(max_length=160, required=True, default=None)
    status = fields.BooleanField(default=False, required=False)
    disabled = fields.BooleanField(default=False, required=False)
    auth = fields.DictField()
    roles = fields.ListField(fields.StringField(), required=False, default=['admin'])
    scope = fields.DictField(required=False, default={})
