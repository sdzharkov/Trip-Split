from django.conf.urls import url
from django.views.generic import TemplateView
# from django.contrib.auth.views import login
# from django.contrib.auth.views import logout
from . import views
# from carAPI.views import *

urlpatterns = [
    url(r'^cars/$', views.carsList.as_view()),
    url(r'^gas/$', views.gasList.as_view()),
]





