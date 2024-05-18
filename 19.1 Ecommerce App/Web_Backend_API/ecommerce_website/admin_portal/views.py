from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .forms import ProductModelForm, CategoryModelForm

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.utils import timezone



def admin_or_staff_required(view_func):
    """
    Decorator that checks if the user is an admin or staff member.
    """
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not (request.user.is_staff or request.user.is_superuser):
            return HttpResponse(status=401)  # Or redirect to login page or show a 401 error page
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# Usage example:
@admin_or_staff_required
def admin_portal(request):
    products = Product.objects.all()
    new_products = products.order_by('-created_at')[:10] 

    context = {
        'products':products,
        'new_products': new_products
    }
    return render(request, 'admin_portal/admin_portal.html', context)

@admin_or_staff_required
def add_product(request):
    products = Product.objects.all()
    products_count = products.count()
    new_products_count = products.filter(is_new=True).count()
    out_of_stock_count = products.filter(in_stock=False).count()
    is_listed_count = products.filter(is_listed=True).count()
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    else:
        form = ProductModelForm()
    context = {
        'form': form, 
        'products': products,
        'products_count': products_count,
        'new_products_count': new_products_count,
        'out_of_stock_count': out_of_stock_count,
        'is_listed_count': is_listed_count,
    }
    return render(request, 'admin_portal/add_product.html', context)

@admin_or_staff_required
def add_category(request):
    form = CategoryModelForm(request.POST)
    context = {
        'form': form
    }
    pass

@admin_or_staff_required
def inventory(request):
    products = Product.objects.all()
    products_count = products.count()
    new_products_count = products.filter(is_new=True).count()
    out_of_stock_count = products.filter(in_stock=False).count()  
    is_listed_count = products.filter(is_listed=True).count()  
    context = {
        'products': products,
        'products_count': products_count,
        'new_products_count': new_products_count,
        'out_of_stock_count': out_of_stock_count,
        'is_listed_count': is_listed_count,
    }
    return render(request, 'admin_portal/inventory.html', context)

@admin_or_staff_required
def product_inventory(request, pk):
    products = Product.objects.all()
    product = get_object_or_404(Product, id=pk)
    products_count = products.count()
    new_products_count = products.filter(is_new=True).count()
    out_of_stock_count = products.filter(in_stock=False).count
    is_listed_count = products.filter(is_listed=True).count
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory')  
    else:
        form = ProductModelForm(instance=product) 
        
    context = {
        'product': product,
        'form': form,
        'products_count': products_count,
        'new_products_count': new_products_count,
        'out_of_stock_count': out_of_stock_count,
        'is_listed_count': is_listed_count
    }
    return render(request, 'admin_portal/product_inventory.html', context)
