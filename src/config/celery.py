import os
from pathlib import Path
import sys
from celery.schedules import crontab,solar


sys.path.append(str(Path(__file__).resolve().parent.parent))

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'add-every-60-seconds': {
#         'task': 'task_manager.tasks.add',
#         'schedule': 60.0,
#         'args': (16, 16)
#     },
# }


app.conf.beat_schedule = {
    'add-every-3-minutes-40-seconds': {
        'task': 'task_manager.tasks.add',
        'schedule': 220.0,
        'args': (16, 16)
    },

    'add-every-hour-3-times-between-19-21': {
        'task': 'task_manager.tasks.mul',
        'schedule':crontab(minute=0, hour='19-21'),
        'args': (16, 16)
    },

    'sunrise-welcome': {
        'task': 'task_manager.tasks.send_sunrise_welcome',
        'schedule': solar('sunrise', 53.54, 27.33),
    },
}

#
# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')