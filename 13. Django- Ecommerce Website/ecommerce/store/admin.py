from django.contrib import admin
from .models import Category, Product, Customer, Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)