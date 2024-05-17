from rest_framework import serializers
from .models import Category, Product, Rating, Reviews


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'image')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'category', 'discount', 'discounted_price')


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ('product', 'user', 'comment')


class ProductDetailSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'discount', 'reviews')

    def get_reviews(self, instance):
        return ReviewSerializer(instance.product_comment.all(), many=True).data

