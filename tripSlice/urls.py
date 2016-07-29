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
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='index'),
    url(r'^tripapp/', include('tripapp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^login/', auth_views.login, {'template_name':'login.html'},name='login'),
    url(r'^logout/',auth_views.logout_then_login, name='logout'),
    # url(r"^signup/$", views.signup, name="account_signup"),
    # url(r"^login/$", views.login, name="account_login"),
    # url(r"^logout/$", views.logout, name="account_logout"),
    #
    # url(r"^password/change/$", views.password_change,
    #     name="account_change_password"),
    # url(r"^password/set/$", views.password_set, name="account_set_password"),
    #
    # url(r"^inactive/$", views.account_inactive, name="account_inactive"),
    #
    # # E-mail
    # url(r"^email/$", views.email, name="account_email"),
    # url(r"^confirm-email/$", views.email_verification_sent,
    #     name="account_email_verification_sent"),
    # url(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email,
    #     name="account_confirm_email"),
    #
    # # password reset
    # url(r"^password/reset/$", views.password_reset,
    #     name="account_reset_password"),
    # url(r"^password/reset/done/$", views.password_reset_done,
    #     name="account_reset_password_done"),
    # url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
    #     views.password_reset_from_key,
    #     name="account_reset_password_from_key"),
    # url(r"^password/reset/key/done/$", views.password_reset_from_key_done,
    #     name="account_reset_password_from_key_done"),
]
