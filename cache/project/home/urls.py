from django.urls import path
from . import views
urlpatterns = [
    path("",views.home),
    path("cache",views.cache,name="cache")

]