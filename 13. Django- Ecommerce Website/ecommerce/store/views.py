from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'store/home.html')

def product(request):
    return render(request, 'store/product.html')

def user_register(request):
    return render(request, 'store/register.html')

def user_login(request):
    return render(request, 'store/login.html')

def user_logout(request):
    return render(request, 'store/home.html')
