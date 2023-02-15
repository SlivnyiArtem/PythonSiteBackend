from django.contrib import admin

from app.internal.models.simple_user import SimpleUser

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"
admin.site.register(SimpleUser)
