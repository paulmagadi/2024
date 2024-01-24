from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    is_sale = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)
    discount = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='images/products/')
    
    def __str__(self):
        return f"{self.name} {self.price}"
    
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/customers/')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# class Order(models.Model):
    
    