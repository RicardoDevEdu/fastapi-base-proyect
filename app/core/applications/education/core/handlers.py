import json
from typing import Optional
from app.core.applications.education.core.services.materialservice import MaterialService
from app.core.applications.education.core.serializable import (
    RequestMaterial
)


class EducationHandler:

    @staticmethod
    def create(data: RequestMaterial):
        sevice = MaterialService()
        model = sevice.create_material(data)
        return json.loads(model.to_json())

    @staticmethod
    def update(id: str, data: RequestMaterial):
        sevice = MaterialService()
        sevice.get(id)
        return dict(uuid=sevice.update_material(id, data))

    @staticmethod
    def list(q: Optional[str] = None):
        sevice = MaterialService()
        models = sevice.list(q)
        return json.loads(models.to_json())

    @staticmethod
    def delete(id: str):
        sevice = MaterialService()
        return dict(uuid=sevice.delete(id))

    @staticmethod
    def get(id: str):
        sevice = MaterialService()
        return sevice.get_material(id)
