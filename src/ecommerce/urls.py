from django.urls import path
from ecommerce import views

urlpatterns = [
    path('', views.product_list_view, name='home'),
    path('<int:product_id>/', views.product_detail_view, name='detail'),
    path('create/', views.product_create_view, name='create'),
    path('<int:product_id>/edit/', views.product_update_view, name='update'),
    path('<int:product_id>/delete/', views.product_delete_view, name='delete'),

]