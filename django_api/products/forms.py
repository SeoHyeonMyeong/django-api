from cgi import print_exception
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField()
    description = forms.CharField()
    price       = forms.DecimalField()
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
        