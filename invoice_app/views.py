from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import InvoiceForm
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


def display_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            context = {
                'description': form.cleaned_data['description'],
                'quantity': form.cleaned_data['quantity'],
                'unit_price': form.cleaned_data['unit_price'],
                'address': form.cleaned_data['address'],
            }
            return render(request, 'invoice_app/invoice_display.html', context)
    return redirect('invoice_page')

# def invoice_page(request):
#     if request.method == 'POST':
#         form = InvoiceForm(request.POST)
#         if form.is_valid():
#             return generate_pdf_invoice(form.cleaned_data)
#     else:
#         form = InvoiceForm()

#     return render(request, 'invoice_app/invoice_page.html', {'form': form})

def invoice_page(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            context = {
                'description': form.cleaned_data['description'],
                'quantity': form.cleaned_data['quantity'],
                'unit_price': form.cleaned_data['unit_price'],
                'address': form.cleaned_data['address'],
            }
            return render(request, 'invoice_app/invoice_display.html', context)
    else:
        form = InvoiceForm()
    
    return render(request, 'invoice_app/invoice_page.html', {'form': form})



