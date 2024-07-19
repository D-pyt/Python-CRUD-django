from django.db import models


class Star(models.Model):
    star_name = models.CharField(max_length=50, unique=True, blank=False)
    star_constellation = models.TextField(max_length=50, null=True, blank=True)
    star_type = models.TextField(max_length=50, null=True, blank=True)
    star_distance = models.TextField(max_length=25, null=True, blank=True)
    star_mass = models.TextField(max_length=25, null=True, blank=True)
    star_temperature = models.TextField(max_length=25, null=True, blank=True)
    star_period = models.TextField(max_length=25, null=True, blank=True)
    star_turn_speed = models.TextField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f'Star: {self.star_name} {self.star_constellation}'
