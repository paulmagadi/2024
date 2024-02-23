from django.shortcuts import render
from .models import Product


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
    product = Product.objects.filter(id=pk)
    context = {
        'product': product
    }
    return render(request, 'store/product.html', context)


def category(request):
    return render(request, 'store/category.html')


def sale(request):
    return render(request, 'store/sale.html')


def new(request):
    return render(request, 'store/new.html')


def featured(request):
    return render(request, 'store/featured.html')


def offers(request):
    return render(request, 'store/offers.html')