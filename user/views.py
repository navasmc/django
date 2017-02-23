from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import  login  as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import LoginForm,RegisterForm
# Create your views here.
##Login
def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':       
        form = LoginForm(request.POST)
        if form.is_valid():          
           user = form.login(request)
           if user:
            auth_login(request, user)
            return HttpResponseRedirect("/user/")# Redirect to a success page.
           else:       
            # redirect to a new URL:
            return HttpResponseRedirect('/login/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/user/login/')        
    return render(request, 'home.html', {})  

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/user/login/')
##Registration
def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':       
        form = RegisterForm(request.POST)
        if form.is_valid():          
           user = form.register(request)
           if user:
            auth_login(request, user)
            return HttpResponseRedirect("/user/")# Redirect to a success page.
           else:       
            # redirect to a new URL:
            return HttpResponseRedirect('/login/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})