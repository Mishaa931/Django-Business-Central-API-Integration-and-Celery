# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings 
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
from celery.schedules import crontab
app = Celery('project')

app.conf.enable_utc=False
app.conf.update(timezone='Asia/Karachi')

# CELERY_BEAT_SCHEDULE = {
#     'fetch-and-store-data-after-five-minutes': {
#         'task': 'app1.tasks.itemSalePriceDataImport',
#         'schedule': crontab(second=10), 
#     },
# }

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

