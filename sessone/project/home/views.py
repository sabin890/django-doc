
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home/home.html")

def setsession(request):
    request.session["name"]='sabin'
    request.session["address"]='raniban'
    return render(request,"home/set.html")
 
def getsession(request):
    # name=request.session["name"]
    # address=request.session["address"]
    name=request.session.get('name', default="guest")
    Address=request.session.get('address', default="nepal")
    return render(request,"home/session.html",{"uname":name,"add":Address})


def delsession(request):
    if 'name' and 'address' in request.session:
        del request.session['name']
        del request.session['address']
    return render(request,"home/session.html")
