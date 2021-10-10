import os
from enum import Enum

class AwsEnum(Enum):
    AWS_ACCES_KEY = os.getenv('AWS_ACCES_KEY')
    AWS_ACCES_SECRET_KEY = os.getenv('AWS_ACCES_SECRET_KEY')
    AWS_REGION = os.getenv('AWS_REGION')
    S3_BUCKET_DEFAULT = os.getenv('S3_BUCKET_DEFAULT')
    S3_BUCKET_SUBPATH = os.getenv('S3_BUCKET_SUBPATH', '')