from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'team')
    list_filter = ('role', 'team')
    fieldsets = UserAdmin.fieldsets + (
        ('اطلاعات سازمانی', {'fields': ('role', 'phone', 'avatar', 'team', 'upline', 'wallet_balance')}),
    )

admin.site.register(User, CustomUserAdmin)
