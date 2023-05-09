from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.internal.models.admin_user import AuthUser


@admin.register(AuthUser)
class AdminUserAdmin(UserAdmin):
    pass
