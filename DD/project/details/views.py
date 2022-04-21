from django.shortcuts import render

# Create your views here.
def det(request):
    return render(request,'details/det.html',{'title':'Python'})