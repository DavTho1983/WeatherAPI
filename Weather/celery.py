from __future__ import absolute_import, unicode_literals

import requests
import os
from celery import Celery
from Weather.settings import OPEN_WEATHER_API_URL, OPEN_WEATHER_API_KEY

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Weather.settings')
# set the default Django settings module for the 'celery' program.


app = Celery('Weather')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Gets London weather every hour.

    sender.add_periodic_task(10.0, get_weather_task.s(), name='london_weather')
    sender.add_periodic_task(3600.0, get_weather_task.s(), name='london_weather')


@app.task()
def get_weather_task():

    querystring = {"q": "London,UK"}

    headers = {
        'x-api-key': OPEN_WEATHER_API_KEY,
    }

    res = requests.get(OPEN_WEATHER_API_URL, headers=headers, params=querystring).json()
    return res
