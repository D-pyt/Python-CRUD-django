from django.db import models


class Star(models.Model):
    star_name = models.TextField(max_length=50)
    star_constellation = models.CharField(max_length=50)
    star_type = models.CharField(max_length=50)
    star_distance = models.TextField(max_length=25)
    star_mass = models.TextField(max_length=25)
    star_temperature = models.TextField(max_length=25)
    star_period = models.TextField(max_length=25)
    star_turn_speed = models.TextField(max_length=25)

    def __str__(self):
        return f'Star: {self.star_name} {self.star_constellation}'
