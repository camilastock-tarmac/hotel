from tabulate import tabulate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from .serializers import InvoiceItemSerializer
from django.utils import timezone

@api_view(['GET'])
def hola_mundo(request):
    return Response({"mensaje": "Hola mundo"})

@api_view(['POST'])
def create_invoice_pdf(request):
    serializer = InvoiceItemSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    items = request.data['items']
    item_table_data = []
    total = 0

    for item in items:
        name = item['name']
        quantity = item['quantity']
        unit_price = item['unit_price']
        total_price = quantity * unit_price
        total += total_price
        item_table_data.append([
            name,
            quantity,
            f"${unit_price:.2f}",
            f"${total_price:.2f}"
        ])

    item_table_html = tabulate(
        item_table_data,
        headers=["Item name", "Quantity", "Unit ptice", "Total price"],
        tablefmt="html"
    )

    current_date = timezone.now().strftime('%d/%m/%Y')

    context = {
        'id': data.get('id', 'N/A'),
        'date': current_date,
        'name': data['name'],
        'surname': data['surname'],
        'items': item_table_html,
        'total': f"${total:.2f}"
    }

    html_string = render_to_string('invoice_template.html', context)
    with tempfile.NamedTemporaryFile(delete=True) as output:
        HTML(string=html_string).write_pdf(output.name)

        output.seek(0)
        response = HttpResponse(output.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="invoice.pdf"'

        return response