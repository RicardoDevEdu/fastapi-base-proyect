import uuid
from app.core.applications.publication.core.models import Publication
from app.core.applications.publication.core.serializable import (
    RequestPublication
)
from passlib.context import CryptContext
from app.core.commons.services.aws import AwsService
from app.core.commons.services.genericservice import GenericService


class PulicationService(GenericService):
    def __init__(self):
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.aws_service = AwsService()
        super().__init__(Publication)

    def create_publication(self, data: RequestPublication):
        images = []
        for image in data.get('images'):
            file_name = f"{uuid.uuid4()}.{image.get('type')}"
            self.aws_service.upload_file_base64(
                file_name,
                image.get('mime_type'),
                image.get('content')
            )

            images.append((dict(
                url=file_name,
                size=image.get('size')
            )))

        data.update({'images': images})

        return self.create(data)

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
