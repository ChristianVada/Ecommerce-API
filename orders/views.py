from django.shortcuts import render
from .models import Order
from .serializer import OrderSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class OrderListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        lookup_url_kwarg = "product_cart_id"
        serializer.save(status="Placed")


class OrderCreateUpdateDestroyDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdminUser]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
