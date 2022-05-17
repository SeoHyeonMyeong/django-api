from django.http import HttpResponse
from django.shortcuts import render

from .forms import ProductForm
from .models import Product

# Create your views here.
def index_view(request, *args, **kwargs):
    context = {
        "user_name": "Seo",
        "user_id": 123,
        "user_comments": ["hi","what","thisis..."],
    }
    return render(request, "index.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context = {
        'form': form,
    }
    return render(request, "products/create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price,
    }
    return render(request, "products/detail.html", context)