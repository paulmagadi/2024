from django.shortcuts import render

from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)