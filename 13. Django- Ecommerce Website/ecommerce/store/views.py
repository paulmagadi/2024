from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
# from .forms import CreateUserForm
from django.contrib import messages

from .models import Product, Category

import random

# Home page.
def home(request):
    all_products= list(Product.objects.all())
    on_sale = list(Product.objects.filter(is_sale=True))
    new_products = list(Product.objects.filter(is_new=True))
    is_featured = list(Product.objects.filter(is_featured=True))
    
    random.shuffle(all_products)
    random.shuffle(on_sale)
    random.shuffle(new_products)
    random.shuffle(is_featured)
    
    num_products_to_display = 15
    to_display = 5
    products = all_products[:num_products_to_display]
    sale = on_sale[:to_display]
    new = new_products[:to_display]
    featured = is_featured[:to_display]
    context = {
        'products': products,
        'sale': sale,
        'new': new,
        'featured': featured,
    }
    return render(request, 'store/home.html', context)

def product(request):
    return render(request, 'store/product.html')

def user_register(request):
    return render(request, 'store/register.html')

def user_login(request):
    return render(request, 'store/login.html')

def user_logout(request):
    return render(request, 'store/home.html')







# Product page
# def product(request, pk):
#     product = Product.objects.get(id=pk)
#     stock_quantity = product.stock_quantity
#     quantity_list = list(range(1, stock_quantity + 1))
#     context = {
#         'product': product,
#         'stock_quantity': stock_quantity,
#         'quantity_list': quantity_list,
#     }
#     return render(request, 'store/product.html', context)


# # Category
# def category(request, f):
#     f = f.replace('-', ' ')
#     try:
#         category = Category.objects.get(name=f)
#         products = Product.objects.filter(category=category)
#         context = {
#             'products': products,
#             'category': category
#         }
#         return render(request, 'store/category.html', context)
#     except:
#         messages.success(request, ('Category does not exist!!!'))
#         return redirect('home')

# # All Categories
# def all_categories(request):
#     categories = Category.objects.all()
#     return render(request, 'store/all_categories.html', {'categories': categories})

# def on_sale(request):
#     products = Product.objects.filter(is_sale=True).distinct()
#     return render(request, 'store/pages/on_sale.html', {'products': products})

# def new_product(request):
#     products = Product.objects.filter(is_new=True).distinct()
#     return render(request, 'store/pages/new.html', {'products': products})

# def featured(request):
#     products = Product.objects.filter(is_featured=True).distinct()
#     return render(request, 'store/pages/featured.html', {'products': products})

    
    
    
    
    
    
# # User Login    
# def user_login(request):
#     if request.method == "POST":
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)
#             if user is not None: 
#                 login(request, user)
#                 messages.success(request, ('Login sucess!'))
#                 return redirect('home')
#             else:
#                 messages.success(request, ('Error Logging in. Try again!!!'))
#                 return redirect('home')
#     else:
#         return render(request, 'store/login.html')
    
# # User Logout  
# def user_logout(request):
#     logout(request)
#     messages.success(request, ('You have been logged out!!!'))
#     return redirect('home')

# # user Registration
# def register_user(request):
#     form = CreateUserForm()
#     if request.method == "POST":
#         form = CreateUserForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('home')
            
#     return render(request, 'store/register.html', {'form': form})
