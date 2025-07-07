from rest_framework import serializers
from test.models import Category, Product, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= "__all__"


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields= "__all__"