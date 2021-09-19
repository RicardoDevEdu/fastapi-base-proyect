import os
from celery import Celery


celery_app = Celery(
    'tasks',
    broker=os.getenv("CELERY_BROKER_URL"),
    include=['app.core.tasks']
)

celery_app.conf.timezone = os.environ.get('TIME_ZONE')
celery_app.conf.enable_utc = True


@celery_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
