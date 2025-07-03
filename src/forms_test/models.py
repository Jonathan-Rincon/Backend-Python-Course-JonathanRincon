from django.db import models
from django.conf import settings

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug=models.SlugField(unique=True)
    price = models.FloatField()
# Create your models here.
