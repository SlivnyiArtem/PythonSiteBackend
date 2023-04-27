from django.contrib import admin

from app.internal.models.auth_token import Card
from app.internal.models.banking_account import BankingAccount
from app.internal.models.refresh_token import AuthToken
from app.internal.models.simple_user import SimpleUser

# from app.internal.models.access_token import AccessToken

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"
admin.site.register(SimpleUser)
admin.site.register(BankingAccount)
admin.site.register(Card)
# admin.site.register(AccessToken)
admin.site.register(AuthToken)
