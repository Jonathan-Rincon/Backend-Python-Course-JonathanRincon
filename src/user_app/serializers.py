from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, ValidationError, CharField
from rest_framework.response import Response

User = get_user_model()

class RegistrationSerializer(ModelSerializer):
    password2 = CharField(style={"input_type":"password"}, write_only=True)

    class Meta:
        model = User
        fields = ["full_name", "email", "password", "password2"]
        extra_kwargs = {
            "password":{"write_only":True}
        }
    def save(self):
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise ValidationError ({"error": "Password y password deben coincidir"})
        
        email = self.validated_data["email"]

        if User.objects.filter(email=email).exists():
            raise ValidationError ({"error":"Ese correo ya esta regustrado"})
        
        full_name = self.validated_data["full_name"]

        account = User(email=email, full_name=full_name)
        account.set_password(password)
        account.save()

        return account
