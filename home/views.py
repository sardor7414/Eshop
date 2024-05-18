from rest_framework.response import Response
from .models import Category, Product, Rating, ContactUs
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsSuperUser
from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer, ContactUsSerializer


# Create your views here.

class HomePageAPI(APIView):
    def get_queryset(self):
        return Category.objects.all()

    def get(self, request):
        products = Product.objects.order_by('-created_at')
        serializer = CategorySerializer(self.get_queryset(), many=True)
        serializer1 = ProductSerializer(products, many=True)
        return Response({
            'categories': serializer.data,
            'products': serializer1.data
        })


class ShopPageAPI(APIView):

    def get(self, request, pk):
        products = Product.objects.filter(category_id=pk)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductPageAPI(APIView):

    def get(self, request, pk):
        product = Product.objects.filter(id=pk).first()
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)


class ContactUsAPI(APIView):

    def get(self, request):
        contact = ContactUs.objects.all()
        serializer = ContactUsSerializer(contact, many=True)
        return Response(serializer.data)