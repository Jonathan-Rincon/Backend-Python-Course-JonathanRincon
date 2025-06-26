from django.urls import path
from ecommerce import views

urlpatterns = [
    path('', views.product_list_view, name='home'),
    path('<int:product_id>/', views.product_detail_view, name='detail'),
    path('create/', views.product_create_view, name='create'),
    path('<int:product_id>/edit/', views.product_update_view, name='update'),
    path('<int:product_id>/delete/', views.product_delete_view, name='delete'),
    #--------------------Practica 55-------------------
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:product_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:product_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('procesar/', views.procesar_pedido, name='procesar_pedido'),

]