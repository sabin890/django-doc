from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
   return render(request,"base.html")

def about(request):
   return render(request,"about.html")

def page_1(request):
   return render(request,"page_1.html")

def page_2(request):
   return render(request,"page_2.html")

def page_3(request):
   return render(request,"page_3.html")

def page_4(request):
   return render(request,"page_4.html")