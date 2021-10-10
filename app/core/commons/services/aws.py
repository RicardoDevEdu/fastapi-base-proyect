import base64
import io
from typing import Union

import boto3
from mypy_boto3_s3 import S3ServiceResource, S3Client
from mypy_boto3_s3.service_resource import Bucket
from pydash import is_empty

from ..enums.aws import AwsEnum


class AwsService:
    _kwargs = {
        'aws_access_key_id': str(AwsEnum.AWS_ACCES_KEY.value),
        'aws_secret_access_key': str(AwsEnum.AWS_ACCES_SECRET_KEY.value),
        'region_name': str(AwsEnum.AWS_REGION.value)
    }

    _s3_resource = boto3.resource('s3', **_kwargs)

    @property
    def s3_resource(self) -> S3ServiceResource:
        return self._s3_resource

    @property
    def s3_client(self) -> S3Client:
        return self._s3_resource.meta.client

    def s3_bucket(self, name=str(AwsEnum.S3_BUCKET_DEFAULT.value)) -> Bucket:
        return self._s3_resource.Bucket(name)

    @staticmethod
    def prepare_object_key(object_key: str):
        if not is_empty(str(AwsEnum.S3_BUCKET_SUBPATH.value)):
            return f'{AwsEnum.S3_BUCKET_SUBPATH.value}/{object_key}'
        return object_key

    def s3_download_file(self,
                         object_key: str,
                         bucket_name=str(AwsEnum.S3_BUCKET_DEFAULT.value),
                         as_bytes=False
                         ) -> Union[bytes, io.BytesIO]:
        bucket = self.s3_bucket(bucket_name)
        bytes_buffer = io.BytesIO()

        bucket.download_fileobj(Key=object_key, Fileobj=bytes_buffer)

        if as_bytes:
            file_bytes = bytes_buffer.getvalue()
            bytes_buffer.close()
            return file_bytes

        return bytes_buffer

    def s3_download_file_base64(self,
                                object_key: str,
                                bucket_name=str(
                                    AwsEnum.S3_BUCKET_DEFAULT.value)
                                ) -> str:
        file_bytes: bytes = self.s3_download_file(
            object_key, bucket_name, as_bytes=True)

        file_str = base64.b64encode(file_bytes).decode()

        return file_str

    def upload_file_base64(self, file_name: str, mime_type: str, object_base64: str, bucket_name=str(AwsEnum.S3_BUCKET_DEFAULT.value)):
        bucket = self.s3_bucket(bucket_name)
        return bucket.put_object(
            Key=file_name,
            Body=base64.b64decode(object_base64),
            ContentType=mime_type,
        )

    def presigned_url(self, file_name: str, bucket_name=str(AwsEnum.S3_BUCKET_DEFAULT.value)):
        bucket = self.s3_client
        return bucket.generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket': bucket_name, 'Key': file_name},
            ExpiresIn=3600)
