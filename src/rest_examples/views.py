from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.viewsets import ViewSet
from .serializers import TestSerializer


class TestAPIView(APIView):
    """API VIEW de Prueba"""
    serializer_class = TestSerializer

    def get(self, request, format=None):
        """Regresa una lista de caracteristicas de un APIView"""
        apiview_info = [
            "Usa métodos HTTP como funciones(get, post, patch, put, delete)",
            "Es similar a un Django View tradicional",
            "Te da el mayor  control de la lógica de la App",
            "Es mapeado manualmente a los urls"
        ]
        return Response({"message":"Hola", "apiview_info":apiview_info})
    
    def post(self, request):
        """Crea un mensaje con el nombre ingresado"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'hola {name}'
            return Response ({"message":message})
        else:
            return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)
        
    def put (self, request, pk=None):
        """Manejar la actualizacion de un objeto"""
        return Response({"method":"PUT"})
    def patch (self, request, pk=None):
        """Manejar la actualizacion parcial de un objeto"""
        return Response({"method":"PATCH"})
    def delete (self, request, pk=None):
        """Manejar la eliminacionde un objeto"""
        return Response({"method":"DELETE"})
    

class TestViewset(ViewSet):
    serializer_class = TestSerializer
    """Test viewset""" 
    def list(self, request):
        """Regresa un listado de caracteristicas de los Viewsets"""

        viewset_info = [
                "Usa acciones(list, create, retrieve, update, partial_update and delete)",
                "se mapea automaticamente a los URLS usando routers",
                "Provee mas funcionalidad con menos codigo"
            ]
        return Response({"message":"Hola","viewset_info":viewset_info})
    def create(self, request):
        """Crea un mensaje de saludo"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'hola {name}'
            return Response ({"message":message})
        else:
            return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        """Maneja la consulta de un objeto por su id"""
        return Response({"method":"GET"})
    def update(self, request, pk=None):
        """Maneja la actualizacion de un objeto por su id"""
        return Response({"method":"PUT"})
    def partial_update(self, request, pk=None):
        """Maneja la actualizacion parcialde un objeto por su id"""
        return Response({"method":"PATCH"})
    def destroy(self, request, pk=None):
        """Maneja la eliminacion de un objeto por su id"""
        return Response({"method":"DELETE"})
    
    
        
