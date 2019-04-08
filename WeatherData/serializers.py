from rest_framework import serializers
from .models import LondonWeather

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = LondonWeather
        fields = '__all__'