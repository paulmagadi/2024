from .cart import Cart

#Create context processor to allow our cart work on all pages

def cart(request):
    #Return the default data from our Cart
    return {'cart': Cart(request)}