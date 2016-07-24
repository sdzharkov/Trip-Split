from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'tripapp/index.html')
