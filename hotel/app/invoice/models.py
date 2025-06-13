from django.db import models
from guest.models import Guest

# Create your models here.

class Invoice(models.Model):
    invoice_id = models.CharField(max_length=8, unique=True, editable=False)
    date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.invoice_id:
            last_invoice = Invoice.objects.order_by('-invoice_id').first()
            if last_invoice:
                try:
                    last_id = int(last_invoice.invoice_id)
                except ValueError:
                    last_id = 0
                new_id = f"{last_id + 1:08d}"
            else:
                new_id = "00000001"
            self.invoice_id = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice {self.invoice_id} - {self.guest.name if self.guest else 'No guest'}"
