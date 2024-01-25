from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Product


# Home page
def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)

# About page
def about(request):
    return render(request, 'about.html')

# User Login    
def user_login(request):
    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None: 
                login(request, user)
                messages.success(request, ('Login sucess!'))
                return redirect('home')
            else:
                messages.success(request, ('Error Logging in. Try again!!!'))
                return redirect('home')
    else:
        return render(request, 'login.html')
    
# User Logout  
def user_logout(request):
    logout(request)
    messages.success(request, ('You have been logged out!!!'))
    return redirect('home')