from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sales.settings')

app = Celery('sales')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
)

BEAT_TASKS = {
    'create_customers_report': {
        'task': 'core.tasks.create_customers_report',
        'schedule': 60.0
    }
}

app.autodiscover_tasks()
app.conf.beat_schedule = BEAT_TASKS
app.conf.timezone = settings.TIME_ZONE
