from django.db import models

class Invoice(models.Model):
    billing_address = models.TextField()
    invoice_number = models.IntegerField()

class Item(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    item_description = models.TextField()
    item_quantity = models.IntegerField()
    item_rate = models.DecimalField(max_digits=10, decimal_places=2)
