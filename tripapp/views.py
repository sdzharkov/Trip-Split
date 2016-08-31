from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
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
