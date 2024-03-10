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
    

#extend user model

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]
    
    
#unregister
admin.site.unregister(User)

#register

admin.site.register(User, UserAdmin)
    