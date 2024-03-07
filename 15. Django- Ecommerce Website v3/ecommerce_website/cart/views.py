from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
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


@login_required
def checkout(request):
    cart_instance = Cart(request)  
    cart_items = cart_instance.get_prods() 
    cart_quantities = cart_instance.get_quants()
    total_quantity = sum(cart_quantities.values())
    order_total = cart_instance.order_total()
    products = Product.objects.all()

    context = {
        'cart_items': cart_items,
        'cart_quantities': cart_quantities,
        'total_quantity': total_quantity,
        'order_total': order_total,
        'products': products,
    }
    return render(request, 'cart/checkout.html', context)

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('product_id'):
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        
        
        cart.add(product=product, quantity=product_qty, request=request)
        
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        return response

def cart_delete(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		# Call delete Function in Cart
		cart.delete(product=product_id)

		response = JsonResponse({'product':product_id})
		#return redirect('cart_summary')
		return response


def cart_update(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		cart.update(product=product_id, quantity=product_qty)

		response = JsonResponse({'qty':product_qty})
		#return redirect('cart_summary')
		return response