from django.contrib import admin

# Register your models here.
from .models import User, GuestEmail

admin.site.register(User)
admin.site.register(GuestEmail)