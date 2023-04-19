# from decimal import Decimal
# from unittest.mock import MagicMock
#
# import pytest
#
# from app.internal.models.banking_account import BankingAccount
# from app.internal.models.simple_user import SimpleUser
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
# def test_bank_acc() -> BankingAccount:
#     simple_user_1 = SimpleUser.objects.get_or_create(user_id=123, full_username="tzinch")[0]
#     acc = BankingAccount.objects.get_or_create(account_number=100, account_owner=simple_user_1, currency_amount=500)[0]
#     return acc
#
#
# @pytest.fixture(scope="function")
# def test_new_friend_message():
#     user = SimpleUser.objects.get_or_create(
#         user_id=112,
#         full_username="vortex",
#         user_name="John",
#         surname="Doe",
#         phone_number=79506376666,
#         friends=["Krigg"],
#     )[0]
#     message = MagicMock()
#     message.from_user = user
#     message.from_user.id = 112
#     message.text = "@Solanum"
#     return message
#
#
# @pytest.fixture(scope="function")
# def test_new_friend_message_2():
#     user = SimpleUser.objects.get_or_create(
#         user_id=112,
#         full_username="vortex",
#         user_name="John",
#         surname="Doe",
#         phone_number=79506376666,
#         friends=["Krigg", "Solanum"],
#     )[0]
#     message = MagicMock()
#     message.from_user = user
#     message.from_user.id = 112
#     message.text = "@Solanum"
#     return message
#
#
#
#
#
# @pytest.fixture(scope="function")
# def test_mock_bot():
#     bot = MagicMock()
#     return bot
#
#
# @pytest.fixture(scope="function")
# def test_simple_user_for_handlers_2() -> SimpleUser:
#     user = SimpleUser.objects.get_or_create(
#         user_id=112,
#         full_username="vortex",
#         user_name="John",
#         surname="Doe",
#         phone_number=79506376666,
#         friends=["Krigg"],
#     )[0]
#     return user
#
#
# @pytest.fixture(scope="function")
# def test_simple_user_for_handlers() -> SimpleUser:
#     user = SimpleUser.objects.get_or_create(
#         user_id=115,
#         full_username="vortex",
#         user_name="John",
#         surname="Doe",
#         phone_number=79506375555,
#         friends=["Krigg"],
#     )[0]
#     return user
#
#
# @pytest.fixture(scope="function")
# def test_simple_bank_acc_for_handlers() -> BankingAccount:
#     user = SimpleUser.objects.get_or_create(
#         user_id=115,
#         full_username="vortex",
#         user_name="John",
#         surname="Doe",
#         phone_number=79506375555,
#         friends=["Krigg"],
#     )[0]
#     acc = BankingAccount.objects.get_or_create(account_number=10, account_owner=user, currency_amount="25")[0]
#     return acc
#
#
# @pytest.fixture(scope="function")
# def test_simple_bank_acc_for_handlers_2() -> BankingAccount:
#     user = SimpleUser.objects.filter(user_id=115, full_username="Krigg", friends=["vortex"]).first()
#     acc = BankingAccount.objects.get_or_create(account_number=20, account_owner=user, currency_amount="0")[0]
#     return acc
#
#
# @pytest.fixture(scope="function")
# def test_mock_message_2():
#     user = SimpleUser.objects.get_or_create(
#         user_id=115,
#         full_username="vortex",
#         user_name="John",
#         surname="Doe",
#         phone_number=79506375555,
#         friends=["Krigg"],
#     )[0]
#     message = MagicMock()
#     message.from_user = user
#     message.from_user.id = 115
#     message.text = 10
#     return message
