from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,"home/home.html")

def cache(request):
    return render(request,"home/cache.html")