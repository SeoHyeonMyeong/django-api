from django.shortcuts import render, get_list_or_404
from django.views import View

from .models import Article

# Create your views here.
class InstagramView(View):
    def get(self, request):
        obj = get_list_or_404(Article)
        context = {
            "articles": obj
        }
        return render(request, 'instagram/index.html', context)
        