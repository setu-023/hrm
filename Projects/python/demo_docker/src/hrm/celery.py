import os

from django.conf import settings

from celery import Celery
from celery.schedules import crontab

# from salary.tasks import get_total_salary

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hrm.settings')
celery_app = Celery('hrm')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# celery_app.conf.beat_schedule = {
#     'total_salary': {
#         'task': 'salary.tasks.get_total_salary',
#         #'schedule': crontab(),
#          'schedule': 5.0,


#         # 'args': ('hpatel@aaravtech.com','This is sample message.')
#     }
# }


celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)