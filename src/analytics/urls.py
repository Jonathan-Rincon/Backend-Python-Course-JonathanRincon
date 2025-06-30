from django.urls import path

from analytics import views

urlpatterns = [
    path("sales", views.SalesView.as_view(), name="Sales-Analytics"),
    path("sales/data/", views.SalesAjaxView.as_view(), name="Sales-data"),
]
