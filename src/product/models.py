from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Product(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='products')
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return f"/product/products/{self.slug}/"

    def get_edit_url(self):
        return f"/product/my-products/{self.slug}/"
    
    def get_delete_url(self):
        return f"/product/my-products/{self.slug}/delete/"  
    
class DigitalProduct(Product):
    class Meta:
        proxy = True