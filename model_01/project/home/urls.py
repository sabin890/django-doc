from importlib.resources import path
from django import views
from django.urls import path
from . import views
urlpatterns = [
path("",views.home)
]