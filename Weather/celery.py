from __future__ import absolute_import, unicode_literals

import requests
import os
from celery import Celery
from celery.result import ResultBase

from .settings import OPEN_WEATHER_API_URL, OPEN_WEATHER_API_KEY


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Weather.settings')

app = Celery('Weather')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task()
def get_weather_task():

    querystring = {"q": "London,UK"}

    headers = {
        'x-api-key': OPEN_WEATHER_API_KEY,
    }

    res = list(requests.get(OPEN_WEATHER_API_URL, headers=headers, params=querystring).content.collect())

    return res
