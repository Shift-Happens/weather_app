from django.db import models

class WeatherPreference(models.Model):
    show_temperature = models.BooleanField(default=True)
    show_humidity = models.BooleanField(default=True)
    show_wind = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created_at'