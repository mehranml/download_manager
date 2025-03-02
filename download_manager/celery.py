import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "download_manager.settings")

app = Celery("download_manager")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
