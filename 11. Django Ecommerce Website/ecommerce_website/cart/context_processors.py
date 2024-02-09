from .cart import Cart

# This will allow our cart work on all pages

def cart(request):
    return {'cart': Cart(request)}