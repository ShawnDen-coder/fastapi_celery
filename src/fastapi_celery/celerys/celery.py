from celery import Celery
from fastapi_celery.cfg import settings

app = Celery(broker=settings.celery.broker, backend=settings.celery.backend, include=['fastapi_celery.celerys.tasks'])
