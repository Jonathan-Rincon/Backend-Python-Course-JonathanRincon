from django.db import models
from django.urls import reverse
from billing.models import BillingProfile

ADDRESS_TYPE = (
    ("billing", "Billing address"),
    ("shipping", "Shipping address"),
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True, null=True, help_text="Shipping to? Name of the person receiving the package.")
    nickname = models.CharField(max_length=120, blank=True, null=True, help_text="Internal Reference Nickname")
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPE)
    address_line_1 = models.CharField(max_length=120)
    address_line_2 = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default="United States")

    def __str__(self):
       if self.nickname:
           return str(self.nickname)
       return str(self.address_line_1)

    def get_absolute_url(self):
        return reverse("address-update", kwargs={"pk": self.pk})
    
    def get_short_address(self):
        for_name = self.name
        if self.nickname:
            for_name = f"{self.nickname} | {for_name}"
        return f"{for_name} {self.address_line_1}, {self.city}"
    
    def get_address(self):
        for_name = self.name
        if self.nickname:
            for_name = f"{self.nickname} | {for_name}"
        return f"{for_name}\n{self.address_line_1}\n{self.address_line_2 or ''}\n{self.city}, {self.state} {self.postal_code}\n{self.country}"
