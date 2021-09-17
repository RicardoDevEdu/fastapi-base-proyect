
class MongoOperationError(Exception):
    def __init__(self, message, *args):
        super(MongoOperationError, self)\
            .__init__(
            "Mongo operation error: {}".format(message),
            *args
        )
