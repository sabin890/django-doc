from django.shortcuts import render
from home.models import Student

# Create your views here.
def home(request):
    stud=Student.objects.all()
    return render(request,"home/home.html",{'stu':stud})