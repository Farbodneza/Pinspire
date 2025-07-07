from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from test.models import Product, Order, Category
from test.serializers import ProductSerializer, OrderSerializer, CategorySerializer
from test.filters import  ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend]


    def list(self, request, *args, **kwargs):
        products = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(data=products, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)



class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()