from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
import operator
import functools

# Create your models here.
class CarManager(models.Manager):
    def search(self, search_terms):
        terms = [term.strip() for term in search_terms.split()]
        q_objects = []
        for term in terms:
            q_objects.append(Q(car_make__icontains=term))
            q_objects.append(Q(car_model__icontains=term))
            if term.isdigit():
                t = int(term)
                q_objects.append(Q(car_year__exact=t))

        qs = self.get_queryset()
        return qs.filter(functools.reduce(operator.or_, q_objects))

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
    objects = CarManager()
    def __str__(self):
        return "{0} {1} {2}".format(self.car_year, self.car_make, self.car_model)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
