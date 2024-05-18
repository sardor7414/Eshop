from rest_framework import serializers
from .models import Category, Product, Rating, Reviews, Gallery, ContactUs


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

class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ('product', 'photo')


class ProductDetailSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    review_qty = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'discount', 'reviews', 'images', 'review_qty')

    def get_reviews(self, instance):
        return ReviewSerializer(instance.product_comment.all(), many=True).data

    def get_images(self, instance):
        return GallerySerializer(instance.product_image.all(), many=True).data

    def get_review_qty(self, instance):
        return instance.product_comment.count()



class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = ('address', 'phone', 'email')


