from rest_framework import serializers

from ehardware.products.models import Product


class ProductSerializer(serializers.ModelSerializer[Product]):
    class Meta:
        model = Product
        fields = ["id", "nombre", "sku", "presio", "url"]
        extra_kwargs = {
            "url": {"view_name": "api:product-detail", "lookup_field": "pk"},
        }
