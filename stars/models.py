from django.db import models

# Create your models here.
class Stars(models.Model):
    star_name = models.TextField(max_length=50)
    star_constellation = models.CharField(max_length=50)
    star_type = models.CharField(max_length=50)
    star_distance = models.FloatField(max_length=25)  #maybe use floats instead
    star_mass = models.FloatField(max_length=25)
    star_temperature = models.TextField(max_length=25)
    star_period = models.TextField(max_length=25)
    star_turn_speed = models.TextField(max_length=25)

    def __str__(self):
        return f'Stars: {self.star_name} {self.star_constellation}'
       