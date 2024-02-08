from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages

from .models import Product, Category

import random



# Home page.
def home(request):
    all_products= list(Product.objects.all())
    sale = Product.objects.filter(is_sale=True)
    new = Product.objects.filter(is_new=True)
    random.shuffle(all_products)
    
    num_products_to_display = 15
    products = all_products[:num_products_to_display]
    context = {
        'products': products,
        'sale': sale,
        'new': new
    }
    return render(request, 'store/index.html', context)

# Product page
def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'store/product.html', context)
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
        return render(request, 'store/category.html', context)
    except:
        messages.success(request, ('Category does not exist!!!'))
        return redirect('home')

# All Categories
def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'store/all_categories.html', {'categories': categories})

def on_sale(request):
    products = Product.objects.filter(is_sale=True).distinct()
    return render(request, 'store/pages/on_sale.html', {'products': products})

def new_product(request):
    products = Product.objects.filter(is_new=True).distinct()
    return render(request, 'store/pages/new.html', {'products': products})

    
    
    
    
    
    
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
        return render(request, 'store/login.html')
    
# User Logout  
def user_logout(request):
    logout(request)
    messages.success(request, ('You have been logged out!!!'))
    return redirect('home')

# user Registration
def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
            
    return render(request, 'store/register.html', {'form': form})
