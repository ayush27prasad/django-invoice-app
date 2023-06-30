from django.urls import path
from invoice_app.views import invoice_page,invoice

urlpatterns = [
    path('', invoice_page, name='invoice_page'),
    path('invoice/', invoice, name='invoice'),
]
