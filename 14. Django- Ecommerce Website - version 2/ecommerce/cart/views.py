from django.shortcuts import render
from store import views
from store.models import *
from django.http import JsonResponse
import json

# Create your views here.
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items': items, 
        'order': order,
    }    
    return render(request, 'cart/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items': items, 
        'order': order,
    }    
    return render(request, 'cart/checkout.html', context)



def updateCart(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, status=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
        
    return JsonResponse('Item added successfuly', safe=False)
