from django.contrib import admin
from .models import Product, Category, Profile, ShippingAddress, WebBanner, ProductImage, Specification
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(ShippingAddress)
admin.site.register(WebBanner)
admin.site.register(ProductImage)
admin.site.register(Specification)

#add profile info to user
class ProfileInline(admin.StackedInline):
    model = Profile
    
#extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]
    
    
#unregister old user
admin.site.unregister(User)

#register new user

admin.site.register(User, UserAdmin)
    