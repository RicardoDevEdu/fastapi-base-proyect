from app.core.commons.models import DocumentBase


class GenericQuerySet:

    def __init__(self, baseModel: DocumentBase) -> None:
        self.model = baseModel

    def update(self, key, data):
        return self.model.objects(
            **key
        ).update(
            **data
        )

    def create(self, data):
        return self.model.objects.create(
            **data
        )

    def filter(self, data):
        return self.model.objects(
            **data
        )

    def filter_one(self, data):
        return self.model.objects(
            **data
        ).first()

    def filter_all(self, data, skip, limit, order):
        return self.model.objects(
            **data
        ).skip(int(skip)).limit(int(limit)).order_by(order).all()

    def all(self, data):
        return self.model.objects(
            **data
        )

    def update_key(self, key, data, uuid):
        return self.model.objects(
            uuid=uuid
        ).update_one(**{'set__{}'.format(key): data})

    def model(self):
        return self.model
