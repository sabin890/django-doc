import imp
from django.urls import path
from . import views
urlpatterns = [
    path('det/',views.det,name='det')
]