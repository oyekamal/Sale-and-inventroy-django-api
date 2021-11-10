from django.contrib import admin

# Register your models here.
from .models import User
# admin.register.site(User)
admin.site.register(User)