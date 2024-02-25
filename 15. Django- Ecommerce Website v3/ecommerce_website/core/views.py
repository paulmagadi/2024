from django.shortcuts import render


def register_user(request):
    return render(request, 'core/register.html')

def login_user(request):
    return render(request, 'core/login.html')

def logout_user(request):
    pass