from django.db import models
from decimal import Decimal
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.db.models.signals import post_save, pre_save
import os


def upload_image_path(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

User = settings.AUTH_USER_MODEL

class Product(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='products')
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(default=Decimal('39.99'), max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    is_digital = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f"/product/products/{self.slug}/"

    def get_edit_url(self):
        return f"/product/my-products/{self.slug}/"
    
    def get_delete_url(self):
        return f"/product/my-products/{self.slug}/delete/"  
    
    def __str__(self):
        return self.title
    
class DigitalProduct(Product):
    class Meta:
        proxy = True

