from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.accounts.models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Academic Profile Details', {'fields': ('role', 'full_name')}),
    )
    list_display = ('username', 'email', 'full_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_active')