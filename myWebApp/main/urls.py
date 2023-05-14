from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_site, name="home"),
    path('gundone', views.start_site, name="home"),
]
