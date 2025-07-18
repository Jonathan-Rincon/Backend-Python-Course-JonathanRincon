from django.db import models
from django.conf import settings
from datetime import timedelta
from django.urls import reverse
from django.db.models import Q
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,)

from django.core.mail import send_mail
from django.template.loader import get_template
from django.utils import timezone


# Create your models here.

DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, full_name=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Los Usuarios deben tener un email')
        if not password:
            raise ValueError('Los Usuarios deben tener una contraseña')
        user_obj = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )
        user_obj.set_password(password)
        user_obj.is_active = is_active
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None, full_name=None):
        user = self.create_user(
            email,
            password=password,
            full_name=full_name,
            is_staff=True,
        )
        return user
    def create_superuser(self, email, password=None, full_name=None):
        user = self.create_user(
            email,
            password=password,
            full_name=full_name,
            is_staff=True,
            is_admin=True,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name or self.email

    def get_short_name(self):
        return self.email.split('@')[0]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
