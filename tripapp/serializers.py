from rest_framework import serializers
from tripapp.models import Car


class carSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('car_make', 'car_model', 'car_year', 'car_highway_mpg', 'car_city_mpg', 'car_comb_mpg','car_drive','car_cylinder','fuel')