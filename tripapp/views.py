from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .forms import RegForm, googleForm
# Create your views here.


@login_required
def home(request):
    return render(request, 'home.html')


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
            data = {
                'source': source,
                'dest': dest,
                #'miles': ,
            }
            return JsonResponse(data)
        else:
            return HttpResponseRedirect('fuck')
    else:
        form = googleForm()

    return render(request, 'home.html', {'form': form})
