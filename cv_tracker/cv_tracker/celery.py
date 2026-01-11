import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv_tracker.settings')

app = Celery('cv-tracker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch-justjoin-every-minute': {
        'task': 'job_offers.tasks.fetch_justjoin_offers',
        'schedule': 300.0,
        'args': ('Python',),
    },
}
