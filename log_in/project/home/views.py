from django.shortcuts import render
from django.contrib import messages
from .forms import Sabin, SignUp
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import HttpResponseRedirect
# Create your views here.


def sing_up(request):
    if request.method == "POST":
        fm = SignUp(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Created Successfully")
            fm.save()
            fm = SignUp()
    else:
        fm = SignUp()
    return render(request, 'home/home.html', {"me": fm})


def log_in(request):
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Log In Successfully")
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, "home/log.html", {"form": fm})

def user_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=Sabin(request.POST,instance=request.user )
            if fm.is_valid():
                messages.success(request,"!!!Data saved sucessfully!!!")
                fm.save()
        else:
            fm = Sabin(instance=request.user)
        return render(request, "home/profile.html", {"form": fm})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def user_pass(request):
    if request.method == "POST":
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            # messages.success(request,"Your Password Has been Successfully Changed")
            return HttpResponseRedirect('/profile/')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'home/pass.html', {'form': fm})
