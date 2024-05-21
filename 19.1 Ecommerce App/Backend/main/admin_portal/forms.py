from django import forms
from store.models import Product, Category, ProductImage

class ProductModelForm(forms.ModelForm):
    product_images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'image', 'is_sale', 'sale_price', 'in_stock', 'stock_quantity', 'is_new', 'is_featured', 'is_listed']

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()

        if self.cleaned_data.get('product_images'):
            for image in self.files.getlist('product_images'):
                ProductImage.objects.create(product=product, image=image)

        return product
    
class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
