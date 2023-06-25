from django import forms

class InvoiceForm(forms.Form):
    description = forms.CharField(max_length=255)
    quantity = forms.IntegerField()
    unit_price = forms.DecimalField(max_digits=10, decimal_places=2)
    address = forms.CharField(max_length=255)
