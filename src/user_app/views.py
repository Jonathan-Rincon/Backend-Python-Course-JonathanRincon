from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.contrib.auth import get_user_model
User = get_user_model()

from user_app.serializers import RegistrationSerializer

@api_view(['POST'])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            "message": "Registro exitoso",
            "email": user.email,
            "full_name": user.full_name,
            "tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_view(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()  
        return Response({"message": "Logout exitoso"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"error": "Token inválido o no se pudo desactivar"}, status=status.HTTP_400_BAD_REQUEST)


# Opcional: puedes extender la vista de login si necesitas personalizarla
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Puedes personalizar la respuesta si quieres incluir datos del usuario con el token.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(email=request.data.get("email"))
        response.data.update({
            "email": user.email,
            "full_name": user.full_name
        })
        return response
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile_view(request):
    user = request.user  

    return Response({
        "email": user.email,
        "full_name": user.full_name,
        "phone": user.phone,
        "birth_date": user.birth_date,
        "gender": user.gender,
        "address": user.address,
        "city": user.city,
        "postal_code": user.postal_code,
        "country": user.country,
        "is_active": user.is_active,
    }, status=status.HTTP_200_OK)
