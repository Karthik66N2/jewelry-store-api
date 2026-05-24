from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .permissions import IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

    permission_classes = [IsAdminOrReadOnly]

    filterset_fields = ['base_metal', 'category']

    search_fields = ['name', 'description']

    ordering_fields = ['price', 'rating', 'created_at']


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAdminOrReadOnly]