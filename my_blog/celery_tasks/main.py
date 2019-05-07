import os

from celery import Celery

if not os.getenv("DJANGO_SETTINGS_MODULE"):
    os.environ["DJANGO_SETTINGS_MODULE"] = "my_blog.settings"

app = Celery("celery_tasks")

app.config_from_object("celery_tasks.config")

app.autodiscover_tasks(["celery_tasks.email"])