from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import redis

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookStore.settings')
redis_cloud_url = 'redis://default:zC458uUD1TlhnpNc3bAZhPsdHA3r3KlB@redis-17386.c328.europe-west3-1.gce.redns.redis-cloud.com:17386'
app = Celery('bookStore', broker=redis_cloud_url)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
