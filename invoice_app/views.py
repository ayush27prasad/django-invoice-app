from django.shortcuts import render
from django.views import View
from xhtml2pdf import pisa
from datetime import datetime
from .utils import render_to_pdf



def invoice_page(request):
    if request.method == 'POST':
        billing_address = request.POST.get('billingAddress')
        invoice_number = request.POST.get('invoiceNumber')
        current_date = datetime.now().date()
        items = []
        i = 0
        sub_total = 0
        while(request.POST.get('item_rate[%d]'%i) != None):
            quantity = request.POST.get('item_quantity[%d]'%i)
            rate = request.POST.get('item_rate[%d]'%i)
            total = round(int(quantity) * float(rate),2)
            items.append({
                 'description' : request.POST.get('item_description[%d]'%i),
                 'quantity' : quantity,
                 'rate' : rate,
                 'total' :  total
                        })
            sub_total += total
            i+=1   
        tax = round(0.15*sub_total,2)
        net_total = sub_total + tax
        context = {
            'billing_address': billing_address,
            'invoice_number': invoice_number,
            'items': items,
            'sub_total' : sub_total,
            'tax' : tax,
            'net_total' : net_total,
            'current_date' : current_date
                }
        print(render_to_pdf('invoice.html',context))
        return render(request, 'invoice.html', context)
    else:
        return render(request, 'invoice_page.html')

