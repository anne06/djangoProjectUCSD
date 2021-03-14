from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.introduction, name='introduction'),
    path('introduction', views.introduction, name='introduction'),
    path('presentation', views.presentation, name='presentation'),
    path('covidreport', views.covidreport, name='covidreport'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('userinfo', views.userinfo, name='userinfo'),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]
