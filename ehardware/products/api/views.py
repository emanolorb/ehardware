from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ehardware.products.models import Product

from .serializers import ProductSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("id")
    lookup_field = "pk"
    permission_classes = [AllowAny]
