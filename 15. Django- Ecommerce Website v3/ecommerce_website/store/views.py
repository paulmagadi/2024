from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()
    context = {
        'products': products
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