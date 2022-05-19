from django.shortcuts import render
from django.views import View

# Create your views here.
class InstagramView(View):
    def get(self, request):
        return render(request, 'instagram/index.html')
        