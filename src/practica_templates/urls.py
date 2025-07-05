from django.contrib import admin
from django.urls import path

from .views import productos_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', productos_view),
]