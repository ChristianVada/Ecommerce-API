from django.shortcuts import render
from .models import OrderModel
from .serializer import OrderSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class OrderListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer


class OrderCreateUpdateDestroyDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
