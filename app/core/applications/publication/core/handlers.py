import json
from app.core.applications.publication.core.services.publicationservice import PulicationService
from app.core.applications.publication.core.serializable import (
    RequestPublication
)


class PublicationHandler:

    @staticmethod
    def create(data: RequestPublication):
        pulication_sevice = PulicationService()
        user = pulication_sevice.create_publication(data)
        return json.loads(user.to_json())

    @staticmethod
    def update(id: str, data: RequestPublication):
        pulication_sevice = PulicationService()
        pulication_sevice.get(id)
        return dict(uuid=pulication_sevice.update(id, data))

    @staticmethod
    def list():
        pulication_sevice = PulicationService()
        pulications = pulication_sevice.list()
        return json.loads(pulications.to_json())

    @staticmethod
    def delete(id: str):
        pulication_sevice = PulicationService()
        return dict(uuid=pulication_sevice.delete(id))

    @staticmethod
    def get(id: str):
        pulication_sevice = PulicationService()
        return pulication_sevice.get_publications(id)
