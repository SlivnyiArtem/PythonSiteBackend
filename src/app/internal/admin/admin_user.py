from app.internal.models.admin_user import AdminUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(AdminUser)
class AdminUserAdmin(UserAdmin):
    pass
