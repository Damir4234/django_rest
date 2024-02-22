# Create your views here.
from django.shortcuts import render
from rest_framework import generics

from .models import Payment
from .serializer import PaymentSerializer


# Create your views here.
class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    search_fields = ['lesson', 'courses', 'payment_method']
    ordering_fields = ['payment_date']
