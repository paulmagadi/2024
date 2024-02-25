class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        # Check if you have a session, if not create one
        if 'session_key' not in request.session:
            cart = request.session['session_key'] = {}
        
        # Ensure the session works across all pages 
        self.cart = cart
        
        
    # Add product to session
    def add(self, product):
        product_id = str(product.id)
        
        # If the product with the product id is in the session, pass else add it to the session
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        self.session.modified = True
        
        
    # Define the cart length(for updating cart count)
    def __len__(self):
        return len(self.cart)