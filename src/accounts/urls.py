from django.urls import path, include
from django.contrib import admin
from .views import register_view, UserRegisterAPIView, UserListAPIView, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register_view, name='register'),
    path('register/', UserRegisterAPIView.as_view(), name='api-register'),
    path('users/', UserListAPIView.as_view(), name='api-users'),
    path('api/v4/', include(router.urls)),

]

