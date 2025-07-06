from django.shortcuts import render

from rest_framework import views
from rest_framework.response import Response

class ProductAPIView(views.APIView):

    def get(self, request):
        content = {
            "Estas llamando el metodo GET"
        }
        return Response(content)
    def post(self, request):
        content = {
            "Estas llamando el metodo POST"
        }
        return Response(content)
    def put(self, request):
        content = {
            'Estlas llamando el metodo PUT'
        }
        return Response(content)
    def patch(self, request):
        content = {
            'Estas llamando el metodo PATCH'
        }
        return Response(content)
    def delete(self, request):
        content = {
            'Estas llamando el metodo DELETE'
        }
        return Response(content)

# Create your views here.
