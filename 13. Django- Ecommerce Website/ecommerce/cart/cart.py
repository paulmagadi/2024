from store.models import Product

class Cart():
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
            
            
    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.cart:
            # Update the quantity if the product is already in the cart
            self.cart[product_id]['quantity'] += quantity
        else:
            # Add the product to the cart with the specified quantity
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.price)}
        
        self.session.modified = True
        
        
    def get_products(self):
        product_ids = self.cart.keys()
        # Retrieve the products based on the product IDs stored in the cart
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_cart_length(self):
        # Return the length of the cart
        return len(self.cart)
