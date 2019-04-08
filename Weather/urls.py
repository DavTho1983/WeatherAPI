from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('WeatherData.urls')),
    path('admin/', admin.site.urls),
]
