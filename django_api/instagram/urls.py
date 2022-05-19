from django.urls import path
from .views import (
    InstagramView
)

app_name = 'instagram'
urlpatterns = [    
    path('', InstagramView.as_view(), name='instagram-index')
]
