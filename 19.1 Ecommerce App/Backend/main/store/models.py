from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify


from django.utils import timezone      
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
        
class Specification(models.Model):
    name = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name}: {self.value}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    category = models.ForeignKey('Category', default=None, on_delete=models.CASCADE)
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
    specification = models.ManyToManyField('Specification', blank=True, default=1)
    

    def clean(self):
        super().clean()
        if self.stock_quantity < 0:
            raise ValidationError({'stock_quantity': 'Stock quantity cannot be less than 0'})

    def save(self, *args, **kwargs):
        self.full_clean()  
            
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
    
def get_image_filename(instance, filename):
    name = instance.product.name
    slug = slugify(name)
    return "product_images/%s-%s" % (slug, filename)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    product_images = models.ImageField(upload_to='uploads/products', null=True, blank=True)
 
    class Meta:
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.name
    
    @property
    def imageURL(self):
        try:
            url = self.product_images.url
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
