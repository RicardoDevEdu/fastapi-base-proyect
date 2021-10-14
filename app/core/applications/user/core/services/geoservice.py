from app.core.applications.user.core.models import Company
from app.core.applications.user.core.serializable import (
    RequestUpdateUser,
    RequestUser,
    RequestUserCompany
)
from app.core.commons.services.genericservice import GenericService


class GeoService(GenericService):
    def __init__(self):   
        super().__init__(Company)
    
    def location_near(self, lat: float, long: float, max_distance: int):
        models = self.query_set.model.objects(location__near=[lat, long], location__max_distance=max_distance)
        return models