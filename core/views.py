from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserOrdersAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Order.objects.filter(user_id=user_id)