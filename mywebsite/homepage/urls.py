from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Intro.html', views.intro, name="intro"),
    path('Arch.html', views.arch, name="arch"), 
    path('Appl.html', views.appl, name="appl"),
    path('Proto.html', views.appl, name="proto"),
    path('Chall.html', views.appl, name="chall"),
]