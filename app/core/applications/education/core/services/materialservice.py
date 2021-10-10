import uuid
from app.core.applications.education.core.models import Material
from app.core.applications.education.core.serializable import (
    RequestMaterial
)

from app.core.commons.services.aws import AwsService
from app.core.commons.services.genericservice import GenericService


class MaterialService(GenericService):
    def __init__(self):        
        self.aws_service = AwsService()
        super().__init__(Material)

    def create_material(self, data: RequestMaterial):
        image = data.get('image')
        file_name = f"{uuid.uuid4()}.{image.get('type')}"
        self.aws_service.upload_file_base64(
            file_name,
            image.get('mime_type'),
            image.get('content')
        )

        image = dict(
            url=file_name,
            size=image.get('size')
        )

        data.update({'image': image})

        return self.create(data)

    def update_material(self, id: str, data: RequestMaterial):
        image = data.get('image')
        file_name = f"{uuid.uuid4()}.{image.get('type')}"
        self.aws_service.upload_file_base64(
            file_name,
            image.get('mime_type'),
            image.get('content')
        )

        image = dict(
            url=file_name,
            size=image.get('size')
        )

        data.update({'image': image})

        return self.update(id, data)

    def get_material(self,  id: str):
        material = self.get(id)
        material_json = material.to_mongo().to_dict()
        image = material_json.get('image')
 
        material_json.update({'image': {
            "url":self.aws_service.presigned_url(image.get('url')),
            "size":image.get('size')
        }})

        return material_json
