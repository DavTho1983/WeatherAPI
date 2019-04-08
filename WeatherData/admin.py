from django.contrib import admin
from django.conf.locale.en import formats as en_formats
from .models import LondonWeather


@admin.register(LondonWeather)
class LondonWeatherAdmin(admin.ModelAdmin):
    en_formats.DATETIME_FORMAT = "d M Y H:i:s"
    list_display = (
        "datetime",
        "longitude",
        "latitude",
        "main_weather",
        "description",
        "temperature",
        "clouds",
    )
    ordering = ["id"]
