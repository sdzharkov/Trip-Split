from django.conf.urls import url
# from django.contrib.auth.views import login
# from django.contrib.auth.views import logout


from . import views

urlpatterns = [
    url(r'^home/',views.home,name='home'),
    url(r'^register/', views.RegFormView, name='RegForm'),
]
