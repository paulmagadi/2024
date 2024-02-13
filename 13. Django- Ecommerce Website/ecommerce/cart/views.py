from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, 'cart/cart.html')

def chechout(request):
    return render(request, 'cart/checkout.html')