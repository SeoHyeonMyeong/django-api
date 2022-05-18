from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
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
    obj = get_list_or_404(Product)
    print(obj)
    context = {
        'products': obj
    }
    return render(request, "products/list.html", context)

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    obj.id = id
    context = {
        'object': obj
    }
    return render(request, "products/detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "GET":
        obj.delete()
        return redirect('product')
    else:
        raise Http404