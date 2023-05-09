from django.contrib import admin

from app.internal.models.auth_user import AuthUser
from app.internal.models.banking_account import BankingAccount
from app.internal.models.banking_card import Card
from app.internal.models.refresh_token import RefreshToken
from app.internal.models.simple_user import SimpleUser
from app.internal.models.transaction import Transaction

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"
admin.site.register(SimpleUser)
admin.site.register(BankingAccount)
admin.site.register(Card)
admin.site.register(Transaction)
admin.site.register(RefreshToken)
admin.site.register(AuthUser)
