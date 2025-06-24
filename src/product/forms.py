from django import forms

from .models import Product, DigitalProduct

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Título del producto'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Slug del producto'}),
        }