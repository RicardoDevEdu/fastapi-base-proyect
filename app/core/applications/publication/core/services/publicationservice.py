import os
import uuid
from app.core.applications.publication.core.models import Publication
from app.core.applications.publication.core.serializable import (
    RequestPublication
)
from passlib.context import CryptContext
from app.core.commons.helpers import get_imagen_data, get_tags
from app.core.commons.services.aws import AwsService
from app.core.commons.services.genericservice import GenericService


class PulicationService(GenericService):
    def __init__(self):
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.aws_service = AwsService()
        super().__init__(Publication)

    def create_publication(self, data: RequestPublication):
 
        image_data = get_imagen_data(data.get('images'))

        file_name = f"{uuid.uuid4()}.{image_data.get('type')}"
        self.aws_service.upload_file_base64(
            file_name,
            image_data.get('mimetype'),
            image_data.get('content')
            )

        data.update({
            'images': f"{os.getenv('URL_PUBLIC_S3')}{file_name}",
            'tags': get_tags(data.get('tags'))
        })

        return self.create(data)


    def update_publication(self,id: str, data: RequestPublication):
 
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

        data.update({
            'tags': get_tags(data.get('tags'))
        })

        return self.update(id, data)

    def get_publications(self,  id: str):
        publication = self.get(id)
        publication_json = publication.to_mongo().to_dict()
        images = []
        for image in publication_json.get('images'):
            images.append({
                "url":self.aws_service.presigned_url(image.get('url')),
                "size":image.get('size')
            })
        
        publication_json.update({'images': images})

        return publication_json
