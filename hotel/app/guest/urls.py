from django.urls import path
from .views import create_guest, get_all_guests

urlpatterns = [
    path('guests/create', create_guest, name='create_guest'),
    path('guests/all', get_all_guests, name='get_all_guests'),
]