# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'full_name', 'phone',
            'birth_date', 'gender', 'city', 'country',
            'password' 
        ]

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(
            email=validated_data.get('email'),
            full_name=validated_data.get('full_name', ''),
            phone=validated_data.get('phone'),
            birth_date=validated_data.get('birth_date'),
            gender=validated_data.get('gender'),
            city=validated_data.get('city'),
            country=validated_data.get('country'),
        )
        if password:
            user.set_password(password)
        user.save()
        return user