from django.urls import path
from .views import create_item

urlpatterns = [
        path('items/', create_item, name='create-item'),
]