from django.db import models


class LondonWeather(models.Model):

    """Here we are nly concerning ourselves with the first weather item available. Since there may be multiple types
    of weather at a given place and time, a JSOMField might be more appropriate in future versions, using a Postgres
    db. Would also be nice to have an icon mapping to static files."""

    CONDITIONS = (
        ('Thunderstorm', 'Thunderstorm'),
        ('Drizzle', 'Drizzle'),
        ('Rain', 'Rain'),
        ('Snow', 'Snow'),
        ('Mist', 'Mist'),
        ('Smoke', 'Smoke'),
        ('Haze', 'Haze'),
        ('Dust', 'Dust'),
        ('Fog', 'Fog'),
        ('Sand', 'Sand'),
        ('Ash', 'Ash'),
        ('Ash', 'Ash'),

        ('Squall', 'Squall'),
        ('Sand', 'Sand'),
        ('Sand', 'Sand'),
        ('Tornado', 'Tornado'),
    )

    longitude = models.DecimalField(max_digits=5, decimal_places=2)  # from -180.00 to 180.00
    latitude = models.DecimalField(max_digits=4, decimal_places=2)  # from -90.00 to 90
    main_weather = models.CharField(max_length=12, choices=CONDITIONS)
    description = models.CharField(max_length=50)
    temperature = models.DecimalField(max_digits=6, decimal_places=3)
    pressure = models.DecimalField(max_digits=6, decimal_places=2)
    humidity = models.DecimalField(max_digits=3, decimal_places=0)
    min_temp = models.DecimalField(max_digits=6, decimal_places=3)
    max_temp = models.DecimalField(max_digits=6, decimal_places=3)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    wind_direction = models.DecimalField(max_digits=6, decimal_places=3)
    clouds = models.DecimalField(max_digits=3, decimal_places=0)


