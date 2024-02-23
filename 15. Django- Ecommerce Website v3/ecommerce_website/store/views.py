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