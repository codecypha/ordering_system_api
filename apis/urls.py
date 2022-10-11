from django.urls import path
from .views import ProductList , ProductDetail , CustomerList, OrderList, OrderDetail


urlpatterns = [

    path('products/', ProductList.as_view()),
    path('product/<str:pk>', ProductDetail.as_view()),

    # Customer
    path('customer/', CustomerList.as_view()),
 
    # Order
    path('order/', OrderList.as_view()),
    path('order/<str:pk>', OrderDetail.as_view()),
]