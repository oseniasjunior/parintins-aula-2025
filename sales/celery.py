from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sales.settings')

app = Celery('sales')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
)

app.autodiscover_tasks()
app.conf.timezone = settings.TIME_ZONE
