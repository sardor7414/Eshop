from rest_framework import serializers
from .models import Category, Product, Rating


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'image')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'category', 'discount', 'discounted_price')