from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import InvoiceForm
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


class GenerateInvoicePDF(View):
    def get(self, request):
        form = InvoiceForm()
        return render(request, 'invoice_app/invoice_page.html', {'form': form})

    def post(self, request):
        form = InvoiceForm(request.POST)
        if form.is_valid():
            context = {
                'description': form.cleaned_data["description"],
                'quantity': form.cleaned_data["quantity"],
                'unit_price': form.cleaned_data["unit_price"],
                'address': form.cleaned_data["address"],
            }
            return render(request, 'invoice_app/invoice_details.html', context)
        else:
            return redirect('invoice_page')


def invoice_page(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            return generate_pdf_invoice(form.cleaned_data)
    else:
        form = InvoiceForm()

    return render(request, 'invoice_app/invoice_page.html', {'form': form})

def generate_pdf_invoice(request, data):
    context = {
        'description': data["description"],
        'quantity': data["quantity"],
        'unit_price': data["unit_price"],
        'address': data["address"],
    }
    return render(request, 'invoice_app/invoice_display.html', context)

# def generate_pdf_invoice(data):
#     template = get_template('invoice_app/invoice_template.html')
#     context = {
#         'description': data['description'],
#         'quantity': data['quantity'],
#         'unit_price': data['unit_price'],
#         'address': data['address'],
#     }
#     html = template.render(context)

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('Error generating PDF')

#     return response
