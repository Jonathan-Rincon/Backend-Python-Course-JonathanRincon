from django.urls import path
from django.contrib import admin
from .views import register_view, UserRegisterAPIView, UserListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register_view, name='register'),
    path('register/', UserRegisterAPIView.as_view(), name='api-register'),
    path('users/', UserListAPIView.as_view(), name='api-users'),


]

