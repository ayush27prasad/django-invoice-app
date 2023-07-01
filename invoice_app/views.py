from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .models import Invoice, Item

def invoice_page(request):
    if request.method == 'POST':
        billing_address = request.POST.get('billingAddress')
        invoice_number = request.POST.get('invoiceNumber')
        items = []
        i = 0
        sub_total = 0
        while(request.POST.get('item_rate[%d]'%i) != None):
            quantity = request.POST.get('item_quantity[%d]'%i)
            rate = request.POST.get('item_rate[%d]'%i)
            total = int(quantity) * float(rate)
            items.append({
                 'description' : request.POST.get('item_description[%d]'%i),
                 'quantity' : quantity,
                 'rate' : rate,
                 'total' :  total
                        })
            sub_total += total
            i+=1   

        context = {
            'billing_address': billing_address,
            'invoice_number': invoice_number,
            'items': items,
            'sub_total' : sub_total
                }
        return render(request, 'invoice.html', context)
    else:
        return render(request, 'invoice_page.html')

# def invoice(request):
#     if request.method == 'POST':
#         billing_address = request.POST.get('billingAddress')
#         invoice_number = request.POST.get('invoiceNumber')
#         item_descriptions = request.POST.getlist('item_description[]')
#         item_quantities = request.POST.getlist('item_quantity[]')
#         item_rates = request.POST.getlist('item_rate[]')

#         items = []
#         for description, quantity, rate in zip(item_descriptions, item_quantities, item_rates):
#             item = {
#                 'description': description,
#                 'quantity': quantity,
#                 'rate': rate
#             }
#             items.append(item)

#         context = {
#             'billing_address': billing_address,
#             'invoice_number': invoice_number,
#             'items': items
#         }
#         return render(request, 'invoice.html', context)

#     return render(request, 'invoice.html')
def invoice(request):
    billing_address = request.POST.get('billingAddress')
    invoice_number = request.POST.get('invoiceNumber')
    item_descriptions = request.POST.getlist('item_description[]')
    item_quantities = request.POST.getlist('item_quantity[]')
    item_rates = request.POST.getlist('item_rate[]')
    items = []
    for description, quantity, rate in zip(item_descriptions, item_quantities, item_rates):
            item = {
                'description': description,
                'quantity': quantity,
                'rate': rate
            }
            items.append(item)

    context = {
            'billing_address': billing_address,
            'invoice_number': invoice_number,
            'items': items
    }
    return render(request, 'invoice.html', context)