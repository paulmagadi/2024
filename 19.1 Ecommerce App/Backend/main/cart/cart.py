from store.models import Product
from users.models import Profile
from django.contrib import messages

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        self.request = request
        
        cart = self.session.get('session_key')
        # Check if you have a session, if not create one
        if 'session_key' not in request.session:
            cart = request.session['session_key'] = {}
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
                messages.success(request, ('Product updated to cart.'))
        else:
            # If the product is not in the cart, add it with the requested quantity, limiting it to the available inventory if necessary
            if quantity > available_quantity:
                self.cart[product_id] = available_quantity
                messages.warning(request, f"Quantity limit reached for {product.name}. Cart updated to maximum available quantity.")
            else:
                self.cart[product_id] = quantity
                messages.success(request, ('Product added to cart'))
            
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

    
    
    
    
# from django.contrib import messages
# from store.models import Product
# from users.models import Profile

# class Cart:
#     def __init__(self, request):
#         self.session = request.session
#         self.request = request
#         cart = self.session.get('session_key')
        
#         if 'session_key' not in self.session:
#             cart = self.session['session_key'] = {}
#         self.cart = cart

#     def add(self, request, product, quantity):
#         product_id = str(product.id)
#         available_quantity = product.stock_quantity

#         if product_id in self.cart:
#             total_quantity = self.cart[product_id] + quantity
#             if total_quantity > available_quantity:
#                 self.cart[product_id] = available_quantity
#                 messages.warning(request, f"Quantity limit reached for {product.name}. Cart updated to maximum available quantity.")
#             else:
#                 self.cart[product_id] = total_quantity
#                 messages.success(request, 'Product updated in cart.')
#         else:
#             if quantity > available_quantity:
#                 self.cart[product_id] = available_quantity
#                 messages.warning(request, f"Quantity limit reached for {product.name}. Cart updated to maximum available quantity.")
#             else:
#                 self.cart[product_id] = quantity
#                 messages.success(request, 'Product added to cart.')
        
#         self.session.modified = True
#         self._update_user_cart()

#     def update(self, request, product, quantity):
#         product_id = str(product.id)
#         available_quantity = product.stock_quantity

#         if quantity > available_quantity:
#             self.cart[product_id] = available_quantity
#             messages.warning(request, f"Quantity limit reached for {product.name}. Cart updated to maximum available quantity.")
#         else:
#             self.cart[product_id] = quantity
#             messages.success(request, 'Cart updated successfully.')

#         self.session.modified = True
#         self._update_user_cart()

#     def _update_user_cart(self):
#         if self.request.user.is_authenticated:
#             current_user = Profile.objects.filter(user=self.request.user).first()
#             if current_user:
#                 cart_dict = str(self.cart).replace("'", '"')
#                 current_user.old_cart = cart_dict
#                 current_user.save()

#     def __len__(self):
#         return sum(self.cart.values())

#     def get_prods(self):
#         product_ids = self.cart.keys()
#         products = Product.objects.filter(id__in=product_ids)

#         for product in products:
#             product.quantity = self.cart[str(product.id)]
#             if product.is_sale:
#                 product.total_price = product.sale_price * product.quantity
#             else:
#                 product.total_price = product.price * product.quantity

#         return products

#     def get_quants(self):
#         return self.cart

#     def delete(self, product):
#         product_id = str(product.id)
#         if product_id in self.cart:
#             del self.cart[product_id]
#             messages.success(self.request, f"{product.name} removed from cart.")

#         self.session.modified = True
#         self._update_user_cart()

#     def order_total(self):
#         total = 0
#         for product_id, quantity in self.cart.items():
#             product = Product.objects.get(id=product_id)
#             if product.is_sale:
#                 total += product.sale_price * quantity
#             else:
#                 total += product.price * quantity
#         return total

#     def db_add(self, product, quantity):
#         product_id = str(product.id)
#         if product_id not in self.cart:
#             self.cart[product_id] = int(quantity)

#         self.session.modified = True
#         self._update_user_cart()

    
        