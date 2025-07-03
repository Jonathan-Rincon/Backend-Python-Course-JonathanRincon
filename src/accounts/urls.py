from django.urls import path
from django.contrib import admin
from .views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register_view, name='register'),
]

