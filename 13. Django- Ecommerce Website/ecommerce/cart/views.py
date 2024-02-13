from django.shortcuts import render
from store import views

# Create your views here.
def cart(request):
    return render(request, 'cart/cart.html')

def checkout(request):
    return render(request, 'cart/checkout.html')