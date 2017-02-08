from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework import authentication, permissions, viewsets, filters
from django.contrib.postgres.search import SearchVector
from .forms import *
from .models import *
from .serializers import *
import requests, json
from django_filters import rest_framework as filters
import django_filters
from dal import autocomplete
from django import forms
from django.views.generic.edit import FormView
from django.views import View, generic
from bs4 import BeautifulSoup


class carFilter(filters.FilterSet):
    car_year = filters.CharFilter(name="car_year")
    car_make = filters.CharFilter(name="car_make",lookup_expr='icontains')
    car_model = filters.CharFilter(name="car_model",lookup_expr='icontains')
    fuel = filters.CharFilter(name="fuel")
    car_cylinder = filters.CharFilter(name="car_cylinder")


    class Meta:
        model = Car
        fields = ['car_year', 'car_make', 'car_model']


class carsList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = carSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = carFilter

    def get(self, request,format=None):
        cars = Car.objects.all()
        car_filter=carFilter(request.GET,queryset=cars)
        serializer = carSerializer(car_filter, many=True)
        return Response(serializer.data)


class gasList(generics.ListAPIView):
    def get(self, request,format=None):
        r = requests.get("https://www.gasbuddy.com/USA")
        soup = BeautifulSoup(r.content, "html.parser")
        links = soup.find_all("div", "col-sm-6 col-xs-6 siteName")
        tests = soup.find_all("div", "col-sm-2 col-xs-3 text-right")
        newDict = {}
        for i in range(len(links)):
            link = links[i]
            test = tests[i]
            newDict[str(link.contents[0].strip())] = str(test.contents[0].strip())

        return JsonResponse(newDict)
# class DefaultsMixin(object):
#     """Default settings for view authentication, permissions,
#     filtering and pagination."""

#     authentication_classes = (
#         authentication.BasicAuthentication,
#         authentication.TokenAuthentication,
#     )
#     permission_classes = (
#         permissions.IsAuthenticated,
#     )
#     paginate_by = 25
#     paginate_by_param = 'page_size'
#     max_paginate_by = 100
#     filter_backends = (
#         filters.DjangoFilterBackend,
#         django_filters.SearchFilter,
#         filters.OrderingFilter,
#     )

# class carFilter(filters.FilterSet):
#     car_year = filters.CharFilter(name="car_year")
#     car_make = filters.CharFilter(name="car_make",lookup_expr='icontains')
#     car_model = filters.CharFilter(name="car_model",lookup_expr='icontains')
#     fuel = filters.CharFilter(name="fuel")
#     car_cylinder = filters.CharFilter(name="car_cylinder")


#     class Meta:
#         model = Car
#         fields = ['car_year', 'car_make', 'car_model']


# class carsList(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = carSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filter_class = carFilter

#     def get(self, request,format=None):
#         cars = Car.objects.all()
#         car_filter=carFilter(request.GET,queryset=cars)
#         serializer = carSerializer(car_filter, many=True)
#         return Response(serializer.data)

    # def get_queryset(self):
    #     project = Car.objects.all()
    #     print(self)

    #     if project is None:
    #         return self.queryset.none()

    #     return self.queryset \
    #         .filter(car_make="Mercury",car_model="Capri") \
    #         .filter(author=self.request.user)

    # def post(self, request, format=None):
    #     serializer = carSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class carsDetail(APIView):
#     """
#     """
#     def get_object(self, pk):
#         try:
#             return Car.objects.get(pk=pk)
#         except Car.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         cars = self.get_object(pk)
#         serializer = carSerializer(cars)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         cars = self.get_object(pk)
#         serializer = carSerializer(cars, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         cars = self.get_object(pk)
#         cars.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)