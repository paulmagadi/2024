from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderItem, ShippingAddress

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)