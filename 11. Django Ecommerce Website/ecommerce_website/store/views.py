from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages

from .models import Product, Category


# Home page.
def home(request):
    products = Product.objects.all()
        
    return render(request, 'index.html', {'products': products,})

# Product page
def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'product.html', context)
# Category
def category(request, f):
    f = f.replace('-', ' ')
    try:
        category = Category.objects.get(name=f)
        products = Product.objects.filter(category=category)
        context = {
            'products': products,
            'category': category
        }
        return render(request, 'category.html', context)
    except:
        messages.success(request, ('Category does not exist!!!'))
        return redirect('home')

# All Categories
def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'all_categories.html', {'categories': categories})

    
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

# user Registration
def register_user(request):
    forms = CreateUserForm()
    return render(request, 'register.html', {'forms': forms})
