from django.shortcuts import render


def home(request):
    return render(request, 'store/home.html')


def product(request):
    return render(request, 'store/product.html')


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