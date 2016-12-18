from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, Http404, HttpResponse
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


@login_required
def home(request):
    if request.method == 'POST':
        search_form = SearchCarForm(request.POST)
        if search_form.is_valid():
            keywords = search_form.cleaned_data.get('keywords')
            results = Car.objects.search(keywords)[:10]
            return render(request, 'home.html', {'results': results})
    else:
        search_form = SearchCarForm()
    results = Car.objects.none()
    return render(request, 'home.html', {'search_form':search_form, 'results':results})


def RegFormView(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username, password=password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/tripapp/home')
    else:
        form = RegForm()

    return render(request, 'login.html', {'RForm': form})


def mapsView(request):
    if request.method == 'POST':
        form = googleForm(request.POST)
        if form.is_valid():
            print(form)
            source = form.cleaned_data['source']
            dest = form.cleaned_data['dest']
            data = getGoogleData(source, dest)
            print(data['rows'][0]['elements'][0]['status'])
            if data['rows'][0]['elements'][0]['status'] == 'OK':
                durationValue = data['rows'][0]['elements'][0]['duration']['value']
                durationText = data['rows'][0]['elements'][0]['duration']['text']
                distanceValue = data['rows'][0]['elements'][0]['distance']['value']
                distanceText = data['rows'][0]['elements'][0]['distance']['text']
                print(durationValue, durationText, distanceValue, distanceText)
            #return JsonResponse(data)
                return render(request, 'home.html', {'durationValue': durationValue, 'durationText': durationText, 'distanceValue': distanceValue, 'distanceText': distanceText })

        else:
            return HttpResponseRedirect('Error')
    else:
        form = googleForm()

    return render(request, 'home.html', {'form': form})


def getGoogleData(source, dest):
    key = "AIzaSyBpw7LjjI-o9K5QqkSW0tG9iEtpM-K0ooo"
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
    params = {'origins': source, 'destinations': dest, 'key': key}
    r = requests.get(url, params=params)
    returnedDist = r.json()
    if returnedDist['status'] == 'OK':
        return returnedDist
    else:
        return error


##########################################################################################

# def carSearchView(request):
#     if request.method == 'POST':
#         form = SearchCarForm(request.POST)
#         if form.is_valid():
#             x = form.cleaned_data['carSearch']
#             results = Car.objects.annotate(search=SearchVector('car_year', 'car_model', 'car_make'),).filter(search = x)
#             print(results)
#             return render(request, 'home.html', {'results': results})

#         else:
#             return HttpResponseRedirect('Error')
#     else:
#         form = SearchCarForm()

#     return render(request, 'home.html', {'form': form})

class carSearchView(View):    # A class based view for our car search view 
    form_class = SearchCarForm
    initial = {'key': 'value'}
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            x = form.cleaned_data['carSearch']
            results = Car.objects.annotate(search=SearchVector('car_year', 'car_model', 'car_make'),).filter(search = x)
            print(results)
            #return HttpResponse('success')
            return render(request, self.template_name, {'results': results})

        return render(request, self.template_name, {'form': form})

##########################################################################################
#Learning to work with forms, might be useful later for ajax responses 


# class carSearchForm(FormView):
#     template_name = 'home.html'
#     form_class = SearchCarForm
#     success_url = '/thanks/'

#     def form_valid(self,form):   
#         if form.is_valid():
#             x = form.cleaned_data['carSearch']
#             results = Car.objects.annotate(search=SearchVector('car_year', 'car_model', 'car_make'),).filter(search = x)
#             data = serializers.serialize('json',results)
#             #return super(carSearchForm, self).form_valid(form)
#             return HttpResponse(data,'application/json')
#         else:
#             return HttpResponseRedirect('Error')

# class AjaxableResponseMixin(object):
#     """
#     Mixin to add AJAX support to a form.
#     Must be used with an object-based FormView (e.g. CreateView)
#     """
#     def form_invalid(self, form):
#         response = super(AjaxableResponseMixin, self).form_invalid(form)
#         if self.request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#         else:
#             return response

#     def form_valid(self, form):
#         # We make sure to call the parent's form_valid() method because
#         # it might do some processing (in the case of CreateView, it will
#         # call form.save() for example).
#         response = super(AjaxableResponseMixin, self).form_valid(form)
#         if self.request.is_ajax():
#             data = {
#                 #'pk': self.object.pk,
#             }
#             return JsonResponse("x")
#         else:
#             return response

#     def render_to_json_response(self, context, **response_kwargs):
#         """Render a json response of the context."""

#         data = json.dumps(context)
#         response_kwargs['content_type'] = 'application/json'
#         return HttpResponse(data, **response_kwargs)


# class carUpdateView(AjaxableResponseMixin, generic.UpdateView):
#     model = Car
#     fields = ['car_year', 'car_model', 'car_make']
#     form_class = carSearchForm

    # def get(self,request,*args,**kwargs):
    #     data = request.GET
    #     x = data.get("carSearch")
    #     form = SearchCarForm(request.POST)
    #     if form.is_valid():
    #         x = form.cleaned_data['carSearch']
    #         results = Car.objects.annotate(search=SearchVector('car_year', 'car_model', 'car_make'),).filter(search = x)
    #         data = serializers.serialize('json',results)
    #         mimetype = 'application/json'
    #         return HttpResponse(data, mimetype)









# autocomplete stuff 


# class carAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         # Don't forget to filter out results depending on the visitor !
#         if not self.request.user.is_authenticated():
#             return Car.objects.none()

#         qs = Car.objects.all()

#         if self.q:
#             qs = qs.filter(name__istartswith=self.q)

#         return qs

# class AutoCompleteView(FormView):
#     def get(self,request,*args,**kwargs):
#         data = request.GET
#         username = data.get("username")
#         if username:
#             users = User.objects.filter(username__icontains= username)
#         else:
#             users = User.objects.all()
#             results = []
#             for user in users:
#                 user_json = {}
#                 user_json['id'] = user.id
#                 user_json['label'] = user.username
#                 user_json['value'] = user.username
#                 results.append(user_json)

#             data = json.dumps(results)
#             mimetype = 'application/json'
#             return HttpResponse(data, mimetype)










# #Django Rest Stuff 

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

