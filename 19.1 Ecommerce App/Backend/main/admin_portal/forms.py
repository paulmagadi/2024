from django import forms
from store.models import Product, Category, ProductImage
from django.forms.widgets import ClearableFileInput

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result
# class ProductModelForm(forms.ModelForm):
#     product_images = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}), required=False)

#     class Meta:
#         model = Product
#         fields = ['name', 'price', 'category', 'description', 'image', 'is_sale', 'sale_price', 'in_stock', 'stock_quantity', 'is_new', 'is_featured', 'is_listed']

#     def save(self, commit=True):
#         product = super().save(commit=False)
#         if commit:
#             product.save()

#         if self.cleaned_data.get('product_images'):
#             for image in self.files.getlist('product_images'):
#                 ProductImage.objects.create(product=product, image=image)

#         return product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'image', 'is_sale', 'sale_price', 'in_stock', 'stock_quantity', 'is_new', 'is_featured', 'is_listed']

# class ProductImageForm(forms.ModelForm):
#     product_images = forms.ImageField(widget=MultipleFileInput(attrs={'multiple': True}), required=False)

#     class Meta:
#         model = ProductImage
#         fields = ['product_images']
   
class ProductImageForm(forms.Form):
    images = MultipleFileField()

    def clean_images(self):
        images = self.files.getlist('images')
        if len(images) > 5:  
            raise forms.ValidationError('You can upload a maximum of 5 images.')
        return images
        
class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
