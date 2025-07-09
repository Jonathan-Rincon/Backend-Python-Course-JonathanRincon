from django.urls import path, include

from .views import TestAPIView, TestViewset

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("test-viewset", TestViewset, basename="test-viewset")

urlpatterns = [
    path("", TestAPIView.as_view()),
    path("", include(router.urls))
]