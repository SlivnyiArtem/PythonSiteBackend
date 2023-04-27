from django.contrib import admin

from app.internal.models.auth_token import AuthToken
from app.internal.models.banking_account import BankingAccount
from app.internal.models.banking_card import Card
from app.internal.models.simple_user import SimpleUser

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"
admin.site.register(SimpleUser)
admin.site.register(BankingAccount)
admin.site.register(Card)
admin.site.register(AuthToken)
