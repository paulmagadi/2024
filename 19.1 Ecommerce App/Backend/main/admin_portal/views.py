from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, ProductImage
from .forms import ProductImageForm, ProductModelForm, CategoryModelForm

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.utils import timezone
from users.decorators import group_required



def admin_or_staff_required(view_func):
    # Decorator that checks if the user is an admin or staff member
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not (request.user.is_staff or request.user.is_superuser):
            return HttpResponse(status=401)  # Or redirect to login page or show a 401 error page
        return view_func(request, *args, **kwargs)
    return _wrapped_view


@group_required('Admin')
def admin_portal(request):
    products = Product.objects.all()
    
    new_products = products.order_by('-created_at')[:10] 

    context = {
        'products':products,
        'new_products': new_products,
        
    }
    return render(request, 'admin_portal/admin_portal.html', context)

def add_product(request):
    products = Product.objects.all()
    images = ProductImage.objects.all()
    products_count = products.count()
    new_products_count = products.filter(is_new=True).count()
    out_of_stock_count = products.filter(in_stock=False).count()
    is_listed_count = products.filter(is_listed=True).count()

    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        image_form = ProductImageForm(request.POST, request.FILES)
        files = request.FILES.getlist('images')
        
        
        if form.is_valid() and image_form.is_valid():
            # product = form.save()
            product = form.save(commit=False)
            product.save()
                            
            for file in files:
                ProductImage.objects.create(product=product, image=file)
            return redirect('add_product')
    else:
        form = ProductModelForm()
    
    context = {
        'form': form, 
        'products': products,
        'images': images,
        'products_count': products_count,
        'new_products_count': new_products_count,
        'out_of_stock_count': out_of_stock_count,
        'is_listed_count': is_listed_count,
    }
    
    return render(request, 'admin_portal/add_product.html', context)


@group_required('Admin')
def add_category(request):
    form = CategoryModelForm(request.POST)
    context = {
        'form': form
    }
    pass

# @admin_or_staff_required
@group_required('Admin')
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

@group_required('Admin')
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
