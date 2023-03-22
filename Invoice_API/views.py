from django.shortcuts import render
from rest_framework import viewsets
from .serializers import InvoiceSerializer
from .models import Invoice
# Create your views here.


class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
