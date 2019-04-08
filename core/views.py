from rest_framework import generics

from django_celery_results.models import TaskResult
from core.serializers import ResultSerializer

# Create your views here.
class ResultAPIView(generics.ListAPIView):
    queryset = TaskResult.objects.all()
    serializer_class = ResultSerializer

# def create(self, res):
#     LondonWeather.objects.create(
#         longitude=res.get('coord', 0).get('lon', 0),
#         latitude=res.get('coord', 0).get('lat', 0),
#         main_weather=res.get('weather', {})[0].get('main', 'Rain'),
#         description=res.get('weather', {})[0].get('description', 'No data'),
#         temperature=res.get('main', {}).get('temp', 0),
#         pressure=res.get('main', {}).get('pressure', 0),
#         humidity=res.get('main', {}).get('humidity', 0),
#         min_temp=res.get('main', {}).get('temp_min', 0),
#         max_temp=res.get('main', {}).get('temp_max', 0),
#         wind_speed=res.get('wind', {}).get('speed', 0),
#         wind_direction=res.get('wind', {}).get('deg', 0),
#         clouds=res.get('clouds', {}).get('all', 0),
#     )