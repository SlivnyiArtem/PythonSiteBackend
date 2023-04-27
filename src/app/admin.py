from django.contrib import admin

from app.internal.models.banking_account import BankingAccount
from app.internal.models.banking_card import Card
from app.internal.models.simple_user import SimpleUser
from internal.models.token import RefreshToken

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"
admin.site.register(SimpleUser)
admin.site.register(BankingAccount)
admin.site.register(Card)
admin.site.register(RefreshToken)
