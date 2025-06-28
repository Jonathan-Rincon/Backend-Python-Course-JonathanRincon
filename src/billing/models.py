from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db.models.signals import post_save, pre_save
from accounts.models import GuestEmail

User = settings.AUTH_USER_MODEL

class BillingProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    customer_id = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("billing:billing-profile", kwargs={"pk": self.pk})

    @property
    def has_card(self):
        return hasattr(self, 'card') and self.card is not None
