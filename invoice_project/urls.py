from django.urls import path
from django.contrib import admin
from invoice_app.views import invoice_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('invoice_page/', invoice_page, name='invoice_page'),
]
