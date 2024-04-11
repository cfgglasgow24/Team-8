# jobSite/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'bio', 'skills', 'language', 'education', 'experience']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'skills', 'language', 'education', 'experience')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
