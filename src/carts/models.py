from django.conf import settings
from django.db import models
from django.utils import timezone
from decimal import Decimal
from django.db.models.signals import post_save, pre_save, m2m_changed

from product.models import Product

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    subtotal = models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2)
    total = models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def is_digital(self):
        qs = self.products.all()
        new_qs = qs.filter(is_digital=False)
        if new_qs.exists():
            return False
        return True
