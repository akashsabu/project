from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'rating', 'image']

    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')

        if not image and not self.instance.pk:
            raise forms.ValidationError("Please upload an image when creating a new product.")

        return cleaned_data