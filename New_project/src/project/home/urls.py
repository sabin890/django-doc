from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('page_1/',views.page_1,name='page_1'),
    path('page_2/',views.page_2,name='page_2'),
    path('page_3/',views.page_3,name='page_3'),
    path('page_4/',views.page_4,name='page_4'),
]
