from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.log_in,name="login"),
    path('',views.sing_up ,name="signup"),
    path('profile/',views.user_profile ,name="profile"),
    path('logout/',views.user_logout ,name="logout"),
    path('pass/',views.user_pass ,name="pass"),

]