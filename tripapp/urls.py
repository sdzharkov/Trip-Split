from django.conf.urls import url
from django.views.generic import TemplateView
# from django.contrib.auth.views import login
# from django.contrib.auth.views import logout
from . import views
from tripapp.views import *

urlpatterns = [
    url(r'^home/',views.home,name='home'),
    url(r'^register/', views.RegFormView, name='RegForm'),
    url(r'^google/', views.mapsView, name='googleForm'),
    url(r'^searchingcar/',carSearchView.as_view(), name='SearchCarForm'),
    url(r'^newsplit/', TemplateView.as_view(template_name="newTrip.html")),
    # url(r'^carsApi/$', views.carsList.as_view()),
    # url(r'^carsApi/(?P<pk>[0-9]+)/$', views.carsDetail.as_view())
    #url(r'^autocomplete/$',carAutocomplete.as_view(), name='autocomplete'),
    #url(r'^autocomplete/$',AutoCompleteView.as_view(), name='autocomplete'),
]

