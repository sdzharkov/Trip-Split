from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

from django.contrib.auth import views

# def change_password(request):
#     template_response = views.password_change(request)
#     # Do something with `template_response`
#     return template_response
