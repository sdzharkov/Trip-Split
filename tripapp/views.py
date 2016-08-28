from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
# Create your views here.
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
    return render(request, 'login.html', {'RForm' : form})
