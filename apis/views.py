from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from .models import OrderProduct, Product, Customer
from .serializers import ProductSerializer, CustomerSerializer, OrderDetailSerializer


# Create your views here.

#Product
class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Customer
class CustomerList(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# Order
class OrderList(ListCreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderDetailSerializer
    

class OrderDetail(RetrieveAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderDetailSerializer 

