from django.shortcuts import render
from .models import Product
import datetime
from django.db.models import Q

def home(request):
    all_products = Product.objects.all()
    products = all_products.filter(is_listed=True)
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


def search(request):
    query = request.GET.get('query')
    products = Product.objects.filter(Q(name__contains=query) | Q(description__contains=query) | Q(category__name__icontains=query))
    context = {
        'query': query,
        'products': products,
    }
    return render(request, 'store/search.html', context)