from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'seller', 'color', 'product_dimensions']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'seller': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'product_dimensions': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Product Title',
            'price': 'Product Price',
            'description': 'Product Description',
            'seller': 'Seller Name',
            'color': 'Product Color',
            'product_dimensions': 'Product Dimensions',
        }
        help_texts = {
            'title': 'Enter the title of the product.',
            'price': 'Enter the price of the product.',
            'description': 'Enter a detailed description of the product.',
            'seller': 'Enter the name of the seller.',
            'color': 'Enter the color of the product.',
            'product_dimensions': 'Enter the dimensions of the product.',
        }