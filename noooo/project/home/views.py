from django.shortcuts import render
from .forms import Student
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        sr=Student(request.POST)
        if sr.is_valid():
            sr.save()
            messages.add_message(request, messages.SUCCESS,'Account Created Sucessfully')
        sr=Student()
    else:
        sr=Student()
    return render(request,"home/home.html",{'me':sr})
