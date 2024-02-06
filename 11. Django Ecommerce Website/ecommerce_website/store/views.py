from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
        
    return render(request, 'index.html', {'products': products,})

def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'product.html', context)


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