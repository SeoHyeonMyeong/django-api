from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request, *args, **kwargs):
    context = {
        "user_name": "Seo",
        "user_id": 123,
        "user_comments": ["hi","what","thisis..."],
    }
    return render(request, "index.html", context)