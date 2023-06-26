from django.urls import path
from invoice_app.views import  invoice_page,display_invoice

urlpatterns = [
    path('', invoice_page, name='invoice_page'),
    path('display-invoice/', display_invoice, name='display_invoice'),
]
