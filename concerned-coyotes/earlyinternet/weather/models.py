from django.utils import timezone
from django.db import models


class Weather(models.Model):

    celsius = models.FloatField()
    fahrenheit = models.FloatField()
    city = models.CharField(max_length=512)
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    day = models.DateField(default=timezone.now)
    latitude = models.FloatField()
    longitude = models.FloatField()
