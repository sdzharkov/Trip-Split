from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.postgres.search import SearchVector
from .forms import *
from .models import *
from .serializers import *
import requests


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


def carSearchView(request):
    if request.method == 'POST':
        form = SearchCarForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data['carSearch']
            print(x)
            results = Car.objects.annotate(search=SearchVector('car_year', 'car_model', 'car_make'),).filter(search = x)
            print(results)
            return render(request, 'home.html', {'results': results})

        else:
            return HttpResponseRedirect('Error')
    else:
        form = SearchCarForm()

    return render(request, 'home.html', {'form': form})


#Django Rest Stuff 

class carsList(APIView):

    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = carSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = carSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class carsDetail(APIView):
    """
    """
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cars = self.get_object(pk)
        serializer = carSerializer(cars)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cars = self.get_object(pk)
        serializer = carSerializer(cars, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cars = self.get_object(pk)
        cars.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
