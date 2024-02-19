from django.shortcuts import render, get_list_or_404
from .cart import Cart
from store.models import *
from django.http import JsonResponse

# Create your views here.
def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_list_or_404(Product, id=product_id)
        cart.add(product=product)
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        return response
