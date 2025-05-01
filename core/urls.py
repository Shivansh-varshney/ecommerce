from django.urls import path
from .views import product_list_api_view, order_create_api_view, user_orders_api_view

urlpatterns = [
    path('products/', product_list_api_view, name="products"),
    path('create_order/', order_create_api_view, name="create_order"),
    path('user_orders/', user_orders_api_view, name="user_orders"),
]