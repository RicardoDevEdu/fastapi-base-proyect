import hashlib
import requests
import io
import json
import logging
import boto3
from botocore.config import Config
import os
import uuid
from datetime import datetime, timedelta
from botocore.exceptions import ClientError
from config.settings.base import config_connection_aws


def add_timestamp_model(data: dict):
    data['uuid'] = uuid.uuid1().__str__()
    data['created_at'] = datetime.now()
    data['updated_at'] = datetime.now()
    data['deleted_at'] = None
    return data


def upload_file(data, bucket: str, object_name: str):
    data['consultation_date'] = datetime.now().__str__()
    data = json.dumps(data)

    s3_client = config_connection_aws()
    try:
        s3_client.upload_fileobj(
            io.BytesIO(data.encode()),
            bucket,
            object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def get_data_s3(path_file: str, bucket: str):
    s3_client = config_connection_aws()
    try:
        return s3_client.generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket': bucket, 'Key': path_file},
            ExpiresIn=3600,
        )
    except ClientError as e:
        logging.error(e)
        return False


def live_cache(date_consultation):
    now = datetime.utcnow()
    date_delta = date_consultation + timedelta(
        days=int(
            os.environ.get('AGILDATA_CACHE')
        ))
    return date_delta > now


def generate_token(salt=None) -> str:
    if salt is None:
        salt = dict()
    hash = str(
        [
            json.dumps(salt),
            uuid.uuid1()
        ]
    ).encode()
    _ = hashlib.sha1(hash)
    return _.hexdigest()


def notify_sns(message: dict, subject: str = "notify"):
    """
    sns = boto3.client(
        'sns',
        region_name=os.getenv("AWS_DEFAULT_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )

    sns.publish(
        TargetArn=os.environ.get("SNS_SIGN_PROCESS_TOPIC"),
        Message=json.dumps({'default': message}),
    )

    Se relaiza consulta al api de aliatu
    """

