from django import views
from django.shortcuts import render
from .forms import register
# Create your views here.
def home(request):
    if request.method =='POST':
        fm=register(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            print(fm.cleaned_data['email'])
            print(fm.cleaned_data['password'])
    else:
        fm=register()
    return render(request,"home/home.html",{"me":fm})
