from app.internal.models.simple_user import SimpleUser
from django.contrib import admin

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"
admin.site.register(SimpleUser)
