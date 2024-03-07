from store.models import Product
from django.contrib import messages

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
    def add(self, request, product, quantity):
        product_id = str(product.id)
        available_quantity = product.stock_quantity  # Assuming 'quantity' is the field representing available inventory in your Product model
        
        # Check if the product with the product id is in the session
        if product_id in self.cart:
            # If the product is already in the cart, calculate the total quantity including the newly requested quantity
            total_quantity = self.cart[product_id] + quantity
            
            # If the total quantity exceeds the available inventory, set the cart quantity to the available inventory and raise a message
            if total_quantity > available_quantity:
                self.cart[product_id] = available_quantity
                messages.warning(request, f"Quantity limit reached for {product.name}. Cart updated to maximum available quantity.")
            else:
                self.cart[product_id] = total_quantity
        else:
            # If the product is not in the cart, add it with the requested quantity, limiting it to the available inventory if necessary
            if quantity > available_quantity:
                self.cart[product_id] = available_quantity
                messages.warning(request, f"Quantity limit reached for {product.name}. Cart updated to maximum available quantity.")
            else:
                self.cart[product_id] = quantity
            
        self.session.modified = True



        
        
    # Define the cart length(for updating cart count)
    def __len__(self):
        return len(self.cart)
    
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        # Add total price for each product based on quantity
        for product in products:
            product.quantity = self.cart[str(product.id)]  # Add quantity to product object
            if product.is_sale:  # Check if product is on sale
                product.total_price = product.sale_price * product.quantity  # Use sale price
            else:
                product.total_price = product.price * product.quantity  # Use regular price
        
        return products

    
    
    def get_quants(self):
        return self.cart
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        
        ourcart = self.cart
        ourcart[product_id] = product_qty
        
        self.session.modified = True
        
        mycart = self.cart
        return mycart
    
    
    def order_total(self):
        total = 0
        for product_id, quantity in self.cart.items():
            product = Product.objects.get(id=product_id)
            if product.is_sale:
                total += product.sale_price * quantity
            else:
                total += product.price * quantity
        return total

    
    
    
    
    
    
        