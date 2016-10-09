from django.conf.urls import url
from django.views.generic import TemplateView

# from django.contrib.auth.views import login
# from django.contrib.auth.views import logout


from . import views

urlpatterns = [
    url(r'^home/',views.home,name='home'),
    url(r'^register/', views.RegFormView, name='RegForm'),
    url(r'^google/', views.mapsView, name='googleForm'),
    url(r'^searchingcar/',views.carSearchView, name='SearchCarForm')
    #url(r'^google/', TemplateView.as_view(template_name="name.html"), name='googleForm'),

]
