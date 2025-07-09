"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("up/", include("up.urls")),
    path("", include("pages.urls")),
    path("ecommerce/", include("ecommerce.urls")), 
    path("product/", include("product.urls")),
    path('forms/', include('forms_test.urls')),
    path('test_templates/', include('test_templates.urls')),
    path('practica_templates/', include('practica_templates.urls')),
    path('register/', include('accounts.urls')),
    path("analytics/", include("analytics.urls")),
    path("api/v1/", include("api.urls")),
    path("api/v2/", include("accounts.urls")),
    path("api/v3/", include("rest_examples.urls")),#<---------------------
    path("admin/", admin.site.urls),
]
if not settings.TESTING:
    urlpatterns = [
        *urlpatterns,
        path("__debug__/", include("debug_toolbar.urls")),
    ]
