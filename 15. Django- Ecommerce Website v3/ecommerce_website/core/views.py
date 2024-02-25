from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# from .forms import CreateUserForm
from django.contrib import messages


def register_user(request):
    return render(request, 'core/register.html')

def login_user(request):
    return render(request, 'core/login.html')

def logout_user(request):
    pass