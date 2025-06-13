from django.db import models
from invoice.models import Invoice

class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.quantity} x ${self.unit_price}"

    @property
    def total_price(self):
        return self.quantity * self.unit_price #chrquear con los chicos si esto queremos guardarlo o no
