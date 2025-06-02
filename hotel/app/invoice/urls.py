from django.urls import path
from .views import hola_mundo, create_invoice_pdf

urlpatterns = [
    path('hola/', hola_mundo, name='hola-mundo'),
    path('create_invoice/pdf/', create_invoice_pdf, name='create-invoice-pdf'),
]