from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.internal.users.db_data.models import AuthUser

# from app.internal.models.auth_user import AuthUser


@admin.register(AuthUser)
class AdminUserAdmin(UserAdmin):
    pass
