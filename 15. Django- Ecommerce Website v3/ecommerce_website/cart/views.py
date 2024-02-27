from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart(request):
    cart_instance = Cart(request)  
    cart_items = cart_instance.get_prods() 
    cart_quantities = cart_instance.get_quants()
    total_quantity = sum(cart_quantities.values())
    order_total = cart_instance.order_total()

    context = {
        'cart_items': cart_items,
        'cart_quantities': cart_quantities,
        'total_quantity': total_quantity,
        'order_total': order_total
    }
    return render(request, 'cart/cart.html', context)



def checkout(request):
    cart_instance = Cart(request)  
    cart_items = cart_instance.get_prods() 
    cart_quantities = cart_instance.get_quants()
    total_quantity = sum(cart_quantities.values())
    order_total = cart_instance.order_total()

    context = {
        'cart_items': cart_items,
        'cart_quantities': cart_quantities,
        'total_quantity': total_quantity,
        'order_total': order_total
    }
    return render(request, 'cart/checkout.html', context)

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('product_id'):
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        
        
        cart.add(product=product, quantity=product_qty)
        
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass