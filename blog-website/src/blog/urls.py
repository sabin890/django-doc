from django.urls import path
from blog import views 

urlpatterns = [
    path("",views.Home,name="home"),
]
