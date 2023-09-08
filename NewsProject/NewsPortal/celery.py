import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')
 
app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.conf.beat_schedule = {
    'weekly_notify': {
        'task': 'news.tasks.weekly_notify',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
    
}

app.autodiscover_tasks()