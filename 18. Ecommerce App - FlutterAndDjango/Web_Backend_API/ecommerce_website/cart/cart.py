from store.models import Product, Profile
from django.contrib import messages

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        self.request = request
        
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
        
        #Logged in user
        if self.request.user.is_authenticated:
            
            #Get current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            
            #convert '' to ""
            cart_dict = str(self.cart)
            cart_dict = cart_dict.replace("\'", "\"")
            current_user.update(old_cart=str(cart_dict))
        
        
    def update(self, request, product, quantity):
        product_id = str(product.id)  # Ensure product_id is retrieved correctly
        available_quantity = product.stock_quantity

        # Check if the requested quantity exceeds the available stock
        if quantity > available_quantity:
            # Limit the quantity to the available stock
            self.cart[product_id] = available_quantity
            messages.warning(request, f"Quantity limit reached for {product.name}. Cart updated to maximum available quantity.")
        else:
            # Update the quantity in the cart
            self.cart[product_id] = quantity
            messages.success(request, 'Cart updated successfully')

        self.session.modified = True
    
        #Logged in user
        if self.request.user.is_authenticated:
            
            #Get current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            
            #convert '' to ""
            cart_dict = str(self.cart)
            cart_dict = cart_dict.replace("\'", "\"")
            current_user.update(old_cart=str(cart_dict))
            
        # Return the updated cart
        return self.cart




        
        
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


    def delete(self, product):
        product_id = str(product)
        # Delete from cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
        
        #Logged in user
        if self.request.user.is_authenticated:
            
            #Get current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            
            #convert '' to ""
            cart_dict = str(self.cart)
            cart_dict = cart_dict.replace("\'", "\"")
            current_user.update(old_cart=str(cart_dict))
    
    
    
    def order_total(self):
        total = 0
        for product_id, quantity in self.cart.items():
            product = Product.objects.get(id=product_id)
            if product.is_sale:
                total += product.sale_price * quantity
            else:
                total += product.price * quantity
        return total
    
    
    # Add product to session
    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        
        # Check if the product with the product id is in the session
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True
        
        #Logged in user
        if self.request.user.is_authenticated:
            
            #Get current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            
            #convert '' to ""
            cart_dict = str(self.cart)
            cart_dict = cart_dict.replace("\'", "\"")
            current_user.update(old_cart=str(cart_dict))

    
    
    
    
    
    
        