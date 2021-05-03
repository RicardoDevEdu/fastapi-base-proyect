import os

import boto3
import pymongo
from botocore.config import Config
from littlenv import littlenv
from mongoengine import connect, disconnect

try:
    littlenv.load()
except:
    pass

API_VERSION = "v0.1"
APP_NAME = os.getenv("APP_NAME", "demo")
APP_DESCRIPTION = os.getenv("APP_DESCRIPTION", "Descripcion demo")
SENTRY = os.getenv("SENTRY", "https://6ecb72f8e4294465bcfa41913285a7fb@o533297.ingest.sentry.io/5652760git add")


async def connect_db():
    """

    :return: connect mongodb
    """
    connect(
        os.environ.get('MONGO_NAME', 'test'),
        host=os.environ.get('MONGO_HOST', 'test'),
        port=int(os.environ.get('MONGO_PORT', 'test')),
        username=os.environ.get('MONGO_USER', 'test'),
        password=os.environ.get("MONGO_PASSWORD", "test"),
        alias=os.environ.get('MONGO_NAME', 'test')
    )


async def close_db():
    disconnect(
        alias=os.environ.get('MONGO_NAME', 'test')
    )


def config_connection_aws(sevice: str = "s3"):
    return boto3.client(
        sevice,
        region_name=os.getenv("AWS_DEFAULT_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        config=Config(
            signature_version='s3v4'
        )
    )


CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
