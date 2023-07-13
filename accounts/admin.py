from django.contrib import admin
from .models import CustomUser, CustomUserManager

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'custom_id',
        'password',
        'username'
    )