from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

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
        return redirect('detail', form.instance.id)
        
    context = {
        'form': form
    }
    return render(request, "products/create.html", context)

def product_list_view(request):
    obj = Product.objects.all()
    print(obj)
    context = {
        'products': obj
    }
    return render(request, "products/list.html", context)

def product_detail_view(request, id):
    obj = Product.objects.get(id=id)
    context = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price,
    }
    return render(request, "products/detail.html", context)