from __future__ import absolute_import, unicode_literals

import requests
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Weather.settings')
from .settings import OPEN_WEATHER_API_KEY, OPEN_WEATHER_API_URL
# set the default Django settings module for the 'celery' program.


app = Celery('Weather')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Gets London weather every hour.

    # sender.add_periodic_task(10.0, get_weather_task.s(), name='london_weather_test')
    sender.add_periodic_task(3600.0, get_weather_task.s(), name='london_weather')


@app.task()
def get_weather_task():

    querystring = {"q": "London,UK"}

    headers = {
        'x-api-key': OPEN_WEATHER_API_KEY,
    }

    res = requests.get(OPEN_WEATHER_API_URL, headers=headers, params=querystring).json()
    from WeatherData.models import LondonWeather
    LondonWeather.objects.create(
            longitude=res.get('coord', 0).get('lon', 0),
            latitude=res.get('coord', 0).get('lat', 0),
            main_weather=res.get('weather', {})[0].get('main', 'Rain'),
            description=res.get('weather', {})[0].get('description', 'No data'),
            temperature=res.get('main', {}).get('temp', 0),
            pressure=res.get('main', {}).get('pressure', 0),
            humidity=res.get('main', {}).get('humidity', 0),
            min_temp=res.get('main', {}).get('temp_min', 0),
            max_temp=res.get('main', {}).get('temp_max', 0),
            wind_speed=res.get('wind', {}).get('speed', 0),
            wind_direction=res.get('wind', {}).get('deg', 0),
            clouds=res.get('clouds', {}).get('all', 0),
    )

    return res
