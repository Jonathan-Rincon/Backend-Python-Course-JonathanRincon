from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["user", "title", "price", "description", "slug", "featured", "active", "is_digital"]