from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    car_make = models.CharField(max_length=150)
    car_model = models.CharField(max_length=150)
    car_year = models.PositiveSmallIntegerField()
    car_highway_mpg = models.PositiveSmallIntegerField()
    car_city_mpg = models.PositiveSmallIntegerField()
    car_comb_mpg = models.PositiveSmallIntegerField()
    car_drive = models.CharField(max_length=100)
    car_cylinder = models.PositiveSmallIntegerField()
    fuel = models.CharField(max_length=100)
    def __str__(self):
        return "{0} {1} {2}".format(self.car_year, self.car_make, self.car_model)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
