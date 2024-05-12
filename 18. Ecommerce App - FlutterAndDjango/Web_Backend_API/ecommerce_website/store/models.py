from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

import datetime
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.user.username
    

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name =  models.CharField(max_length=255)
    email =  models.CharField(max_length=255)
    address1 =  models.CharField(max_length=255)
    address2 =  models.CharField(max_length=255 , null=True, blank=True)
    city =  models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    country =  models.CharField(max_length=255)
    
    
    class Meta:
        verbose_name_plural = "Shipping Address"
        
    
    def __str__(self):
        return f'Shipping Address - {str(self.id)}'    
    
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        
# automate
post_save.connect(create_profile, sender=User)

        

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=8, null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    stock_quantity = models.IntegerField(default=1)
    discount = models.DecimalField(default=0, max_digits=9, decimal_places=2, null=True, blank=True)
    percentage_discount = models.DecimalField(default=0, max_digits=5, decimal_places=0, null=True, blank=True)
    is_new = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_listed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    specifications = models.ManyToManyField(Specification)
    

    def save(self, *args, **kwargs):
        if self.created_at >= timezone.now() - timezone.timedelta(minutes=1):
            self.is_new = False
        else:
            self.is_new = True
            
        
        if self.stock_quantity == 0:
            self.in_stock = False
        else:
            self.in_stock = True
            
       
        if self.is_sale and self.sale_price < self.price:
            self.discount = round(self.price - self.sale_price, 2)
            self.percentage_discount = round((self.discount / self.price) * 100)
        else:
            self.discount = 0
            self.percentage_discount = 0
        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.name
        
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    image = models.FileField(upload_to='uploads/products/', max_length=12, null=True)
    
    class Meta:
        verbose_name_plural = 'Product Images'
    
    
    def __str__(self):
        return self.id
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    
    
    
class WebBanner(models.Model):
    image = models.ImageField(upload_to='uploads/banners/', verbose_name="Image")
    caption = models.CharField(max_length=255, blank=True, null=True, verbose_name="Caption")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    in_use = models.BooleanField(default=False)

    def __str__(self):
        return self.caption  
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url