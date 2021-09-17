from app.core.models import DocumentBase


class GenericQuerySet:

    def __init__(self, baseModel: DocumentBase) -> None:
        self.model = baseModel

    def update(self, key, data):
        return self.model.objects(
            **key
        ).update_one(
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

    def update_key(self, key, data, credit_request_code):
        return self.model.objects(
            code=credit_request_code
        ).update_one(**{'set__{}'.format(key): data})
