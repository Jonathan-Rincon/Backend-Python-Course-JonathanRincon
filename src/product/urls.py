from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView, UpdateView, DeleteView

from product.views import (
    ProductListView, 
    DetailView, 
    DigitalProductListView, 
    ProductIDRedirectView, 
    ProductRedirectView,
    ProtectedProductDetailView,
    ProtectedProductCreateView,
    ProtectedProductDeleteView,
    ProtectedProductUpdateView,
    ProtectedListView  
    )

urlpatterns = [
    path('admin/', admin.site.urls),

    # Example of a static page
    path('about/', TemplateView.as_view(template_name='about.html'), name='about-us'),
    path('about-us/', RedirectView.as_view(url='/product/about/'), name='about-us'),
    path('team/', TemplateView.as_view(template_name='team.html'), name='team'),

    # Product URLs
    path('products/', ProductListView.as_view(), name='product_list'),
    path('digital-products/', DigitalProductListView.as_view(), name='digital_product_list'),
    path('products/<int:pk>/', DetailView.as_view(), name='product_detail'),
    path('products/<slug:slug>/', DetailView.as_view(), name='product_detail_slug_id'),
    #path('products/<slug:slug>/', DetailView.as_view(), name='product_detail_slug'),
    path('p/<slug:slug>/', ProductRedirectView.as_view(), name='product_redirect_slug'),
    path('p/<int:pk>/', ProductIDRedirectView.as_view(), name='product_redirect_pk'),
   #path('my-products/<slug:slug>/', ProtectedProductDetailView.as_view(), name='protected_product_detail_slug'),
    path('my-products/create/', ProtectedProductCreateView.as_view(), name='protected_product_create'),
    path('my-products/<slug:slug>/', ProtectedProductUpdateView.as_view()),
    path('my-products/<slug:slug>/delete/', ProtectedProductDeleteView.as_view(), name='protected_product_detail_slug'),
    path('my-products/', ProtectedListView.as_view(), name='my-product_list'),
]