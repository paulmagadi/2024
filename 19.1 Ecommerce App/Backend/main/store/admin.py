from django.contrib import admin
from .models import Product, Category, WebBanner, ProductImage, Specification
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(WebBanner)
admin.site.register(ProductImage)
admin.site.register(Specification)