from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']