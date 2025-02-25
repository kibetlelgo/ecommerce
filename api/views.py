from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, ProductSerializer,CategorySerializer, OrderSerializer
from products.models import Product, Category
from orders.models import Order
from rest_framework.permissions import IsAuthenticated
from .permissions import CustomPermission

User = get_user_model()

class UserViewSet(ReadOnlyModelViewSet):
    queryset =User.objects.all()
    serializer_class=UserSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, CustomPermission]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer    

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer    