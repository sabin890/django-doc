from django import forms
from django.shortcuts import render
from .forms import Reg
from .models import User
# Create your views here.


def home(request):
    if request.method == 'POST':
        # pi=User.object.get(pk=1)
        fm = Reg(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = Reg()
    return render(request, "home/home.html", {"me": fm})


def page(request):
    return render(request, "home/page1.html")

def details(request,my_id):
    student={'id':my_id}
    return render(request, "home/page2.html",student)


















# from django.shortcuts import render
# from .forms import StudentForm
# # Create your views here.
# def home(request):
#     if request.method == "POST":
#         form = StudentForm(request.POST or None)
#         if form.is_valid():
#             print("yes form is valid !")
#             print(request.POST.get("names"))

#     else:
#         form = StudentForm()
#     return render(request,"home/home.html",{'me':form})
