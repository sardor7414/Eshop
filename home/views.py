from rest_framework.response import Response
from .models import Category, Product, Rating
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsSuperUser
from .serializers import CategorySerializer, ProductSerializer

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

