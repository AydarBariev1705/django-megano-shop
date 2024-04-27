from django.contrib import admin

# Register your models here.
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = 'pk', 'fullName', 'email', 'phone'
    list_display_links = 'pk', 'fullName'
    ordering = 'pk',
