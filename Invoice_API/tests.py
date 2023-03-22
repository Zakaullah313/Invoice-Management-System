from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

client = Client()

class InvoiceTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {
            'date': '2022-01-01',
            'invoice_no': 'INV-001',
            'customer_name': 'John Doe',
            'details': [
                {
                    'description': 'Product A',
                    'quantity': '2',
                    'unit_price': '10.00',
                    'price': '20.00'
                },
                {
                    'description': 'Product B',
                    'quantity': '1',
                    'unit_price': '5.00',
                    'price': '5.00'
                }
            ]
        }
        self.response = self.client.post(
            reverse('invoice-list'),
            self.invoice_data,
            format='json')

    def test_create_invoice(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_invoice(self):
        invoice = Invoice.objects.get()
        serializer = InvoiceSerializer(invoice)
        response = self.client.get(reverse('invoice-detail', kwargs={'pk': invoice.id}))
        self.assertEqual(response.data, serializer.data)
