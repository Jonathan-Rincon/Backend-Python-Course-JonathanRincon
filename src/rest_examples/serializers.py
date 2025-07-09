from rest_framework import serializers

class TestSerializer(serializers.Serializer):
    """Serializar un campo de nombre para muestra APIView"""
    name =serializers.CharField(max_length=15)