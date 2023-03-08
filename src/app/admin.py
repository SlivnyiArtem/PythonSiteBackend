from app.internal.models.simple_user import SimpleUser
from app.internal.models.banking_account import BankingAccount
from app.internal.models.card import Card
from django.contrib import admin

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"
admin.site.register(SimpleUser)
admin.site.register(BankingAccount)
admin.site.register(Card)
