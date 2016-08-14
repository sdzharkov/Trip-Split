"""tripSlice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
#admin.autodiscover()

urlpatterns = [
    url(r'^tripapp/', include('tripapp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_views.login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/',auth_views.logout_then_login, name='logout'),
    url('^', include('django.contrib.auth.urls')),
    #url('^change-password/$', auth_views.password_change, {'template_name': 'change-password.html'}),

    #url(r'^accounts/', include('allauth.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    #url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
]
