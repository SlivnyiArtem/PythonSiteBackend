# from unittest.mock import MagicMock
#
# import pytest
#
# from app.internal.models.banking_account import BankingAccount
# from app.internal.models.banking_card import Card
# from app.internal.models.simple_user import SimpleUser
# # from app.tests.teststests.conftest import test_bank_acc
# from app.tests.conftest import test_bank_acc
#
# @pytest.fixture(scope="function")
# def test_mock_bot():
#     bot = MagicMock()
#     return bot
#
#
# @pytest.fixture(scope="function")
# def test_bank_acc_rec() -> BankingAccount:
#     simple_user_2 = SimpleUser.objects.get_or_create(user_id=223, full_username="nurgle")[0]
#     acc = BankingAccount.objects.get_or_create(account_number=2, account_owner=simple_user_2, currency_amount=0)[0]
#     return acc
#
#
# @pytest.fixture(scope="function")
# def test_bank_acc_3_get() -> BankingAccount:
#     simple_user_3 = SimpleUser.objects.get_or_create(user_id=323, full_username="khorn")[0]
#     acc = BankingAccount.objects.get_or_create(account_number=3, account_owner=simple_user_3,
#                                         currency_amount=500)[0]
#     return acc
#
#
# # @pytest.fixture(scope="function")
# # def test_bank_acc() -> BankingAccount:
# #     simple_user_1 = SimpleUser.objects.create(user_id=123, full_username="tzinch")
# #     acc = BankingAccount.objects.create(account_number=1, account_owner=simple_user_1, currency_amount=500)
# #     return acc
#
# @pytest.fixture(scope="function")
# def another_test_bank_acc():
#     simple_user_2 = SimpleUser.objects.get(user_id=123, full_username="tzinch").first()
#     acc = BankingAccount.objects.get(account_number=9, account_owner=simple_user_2, currency_amount=500).first()
#     return acc
#
#
# @pytest.fixture(scope="function")
# def test_card() -> Card:
#     simple_user = SimpleUser.objects.get_or_create(user_id=323, full_username="khorn")[0]
#     acc = BankingAccount.objects.get_or_create(account_number=3, account_owner=simple_user, currency_amount=500)[0]
#     card = Card.objects.get_or_create(card_number=7777, MM=5, YY=2020, system="VISA", banking_account=acc)[0]
#     return card
#
# @pytest.fixture(scope="function")
# def another_test_card(test_bank_acc) -> Card:
#     simple_user = SimpleUser.objects.get_or_create(user_id=778, full_username="tzinch")[0]
#     acc = test_bank_acc # BankingAccount.objects.get_or_create(account_number=1, account_owner=simple_user, currency_amount=500)[0]
#     card = Card.objects.get_or_create(card_number=8888, MM=5, YY=2020, system="VISA", banking_account=acc)[0]
#     return card
#
# @pytest.fixture(scope="function")
# def test_simple_user() -> SimpleUser:
#     user = SimpleUser.objects.get_or_create(user_id=789, full_username="bloodgod")[0]
#     return user
