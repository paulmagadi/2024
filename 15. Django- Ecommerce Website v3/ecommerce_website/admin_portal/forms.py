from django import forms
from store.models import Product
from store.models import Category

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'image', 'is_sale', 'sale_price', 'in_stock', 'stock_quantity', 'is_new', 'is_featured']
 
class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']