from django.shortcuts import render
from .form import registers
# Create your views here.
def home(request):
    foum=registers()
    return render(request,'home/home.html',{"ff":foum})