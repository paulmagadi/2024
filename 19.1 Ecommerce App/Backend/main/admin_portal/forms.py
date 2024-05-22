from django import forms
from store.models import Product, Category, ProductImage
from django.forms.widgets import ClearableFileInput


# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True

# class MultipleFileField(forms.FileField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'image', 'is_sale', 'sale_price', 'in_stock', 'stock_quantity', 'is_new', 'is_featured', 'is_listed']

    
class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
