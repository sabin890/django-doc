from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def base(request):
    return render(request,'base.html')

def services(request):
    return render(request,'services .html')
