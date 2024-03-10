from django.contrib import admin
from .models import Product, Category, Profile
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)


#add profile info to user

class ProfileInline(admin.StackedInline):
    model = Profile
    

    