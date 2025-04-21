from django.urls import path, include
from .views import *

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name="products"),
    path('create_order/', OrderCreateAPIView.as_view(), name="create_order"),
    path('user_orders/', UserOrdersAPIView.as_view(), name="user_orders")
]