from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import *
from django.http import JsonResponse

# Create your views here.
def cart(request):
    cart = Cart(request)
    cart_products = cart.get_products
    # cart_quantities = cart.get_quantities
    context = {
        'cart_products': cart_products
    }
    return render(request, 'cart/cart.html', context)

# def cart_summary(request):
# 	# Get the cart
# 	cart = Cart(request)
# 	cart_products = cart.get_prods
# 	quantities = cart.get_quants
# 	totals = cart.cart_total()
# 	return render(request, "cart/cart_summary.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals})


    

def checkout(request):
    return render(request, 'cart/checkout.html')
    
    

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        cart_quantity = cart.get_cart_length()  # Use get_cart_length method to get the length of the cart
        response = JsonResponse({'qty': cart_quantity})
        return response

# def cart_delete(request):
# 	cart = Cart(request)
# 	if request.POST.get('action') == 'post':
# 		# Get stuff
# 		product_id = int(request.POST.get('product_id'))
# 		# Call delete Function in Cart
# 		cart.delete(product=product_id)

# 		response = JsonResponse({'product':product_id})
# 		#return redirect('cart_summary')
# 		return response


# def cart_update(request):
# 	cart = Cart(request)
# 	if request.POST.get('action') == 'post':
# 		# Get stuff
# 		product_id = int(request.POST.get('product_id'))
# 		product_qty = int(request.POST.get('product_qty'))

# 		cart.update(product=product_id, quantity=product_qty)

# 		response = JsonResponse({'qty':product_qty})
# 		#return redirect('cart_summary')
# 		return response