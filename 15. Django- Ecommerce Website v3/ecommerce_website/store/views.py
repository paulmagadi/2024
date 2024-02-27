from django.shortcuts import render
from .models import Product

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

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
def admin_dashboard(request):
    return render(request, 'store/admin.html')

def home(request):
    products = Product.objects.all()
    sale_products = products.filter(is_sale=True)
    new_products = products.filter(is_new=True)
    featured_products = products.filter(is_featured=True)
    context = {
        'products': products,
        'sale_products': sale_products,
        'new_products': new_products,
        'featured_products': featured_products,
    }
    return render(request, 'store/home.html', context)


def product(request, pk):
    product = Product.objects.get(id=pk)
    stock_quantity = product.stock_quantity
    context = {
        'product': product,
        'stock_quantity': stock_quantity
    }
    return render(request, 'store/product.html', context)


def category(request):
    return render(request, 'store/category.html')


def sale(request):
    products = Product.objects.filter(is_sale=True)
    return render(request, 'store/sale.html', {'products': products})


def new(request):
    products = Product.objects.filter(is_new=True)
    return render(request, 'store/new.html', {'products': products})
    


def featured(request):
    products = Product.objects.filter(is_featured=True)
    return render(request, 'store/featured.html', {'products': products})


def offers(request):
    return render(request, 'store/offers.html')