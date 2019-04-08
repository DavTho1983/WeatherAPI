from rest_framework import generics

from .models import LondonWeather
from .serializers import ResultSerializer

# Create your views here.
class ResultAPIListView(generics.ListAPIView):
    queryset = LondonWeather.objects.all()
    serializer_class = ResultSerializer


class ResultAPIID(generics.RetrieveAPIView):
    queryset = LondonWeather.objects.all()
    serializer_class = ResultSerializer
