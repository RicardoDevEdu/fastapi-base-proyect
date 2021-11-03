import os
import uuid
from app.core.applications.education.core.models import Material
from app.core.applications.education.core.serializable import (
    RequestMaterial
)
from app.core.commons.helpers import get_imagen_data, get_tags

from app.core.commons.services.aws import AwsService
from app.core.commons.services.genericservice import GenericService


class MaterialService(GenericService):
    def __init__(self):        
        self.aws_service = AwsService()
        super().__init__(Material)

    def create_material(self, data: RequestMaterial):

        
        image_data = get_imagen_data(data.get('images'))

        file_name = f"{uuid.uuid4()}.{image_data.get('type')}"
        self.aws_service.upload_file_base64(
            file_name,
            image_data.get('mimetype'),
            image_data.get('content')
            )

        data.update({
            'images': f"{os.getenv('URL_PUBLIC_S3')}{file_name}"
        })

        return self.create(data)

    def update_material(self, id: str, data: RequestMaterial):
        image_data = get_imagen_data(data.get('images'))

        if image_data is not None:
            file_name = f"{uuid.uuid4()}.{image_data.get('type')}"
            self.aws_service.upload_file_base64(
                file_name,
                image_data.get('mimetype'),
                image_data.get('content')
                )

            data.update({
                'images': f"{os.getenv('URL_PUBLIC_S3')}{file_name}"
            })     

        return self.update(id, data)
 
