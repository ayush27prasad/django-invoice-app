from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


def invoice_page(request):
    if request.method == 'POST':
        billing_address = request.POST.get('billingAddress')
        invoice_number = request.POST.get('invoiceNumber')
        # Retrieve the item details from the request.POST dictionary
        item_descriptions = request.POST.getlist('itemDescription')
        item_quantities = request.POST.getlist('itemQuantity')
        item_unit_prices = request.POST.getlist('itemUnitPrice')
        # Create a list to store the item data
        items = []
        for description, quantity, unit_price in zip(item_descriptions, item_quantities, item_unit_prices):
            item = {
                'description': description,
                'quantity': quantity,
                'unit_price': unit_price
            }
            items.append(item)
        # Pass the data to the template
        context = {
            'billing_address': billing_address,
            'invoice_number': invoice_number,
            'items': items
        }
        return render(request, 'invoice.html', context)
    else:
        return render(request, 'invoice_page.html')

def invoice(request):
    if request.method == 'POST':
        # Retrieve the form data from the POST request
        billing_address = request.POST.get('billingAddress')
        invoice_number = request.POST.get('invoiceNumber')

        # Retrieve the item data from the POST request
        item_descriptions = request.POST.getlist('itemDescription')
        item_quantities = request.POST.getlist('itemQuantity')
        item_prices = request.POST.getlist('itemUnitPrice')

        # Prepare the data to pass to the template
        context = {
            'billing_address': billing_address,
            'invoice_number': invoice_number,
            'items': zip(item_descriptions, item_quantities, item_prices),
        }

        # Render the invoice template with the data
        return render(request, 'invoice.html', context)

    # If the request method is GET, render the initial form
    return render(request, 'invoice.html')
