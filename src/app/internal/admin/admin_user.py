from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.internal.models.admin_user import AdminUser


@admin.register(AdminUser)
class AdminUserAdmin(UserAdmin):
    pass
