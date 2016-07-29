from django.conf.urls import url
from django.conf.urls import include

from . import views

app_name = 'tripapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/',views.home,name='home'),
]
