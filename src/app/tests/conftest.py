# место для фикстур
from unittest.mock import MagicMock

import pytest

from app.internal.models.banking_account import BankingAccount
from app.internal.models.banking_card import Card
from app.internal.models.simple_user import SimpleUser






@pytest.fixture(scope="function")
def test_bank_acc() -> BankingAccount:
    simple_user_1 = SimpleUser.objects.get_or_create(user_id=123, full_username="khorn")[0]
    acc = BankingAccount.objects.get_or_create(account_number=100, account_owner=simple_user_1, currency_amount=500)[0]
    return acc

@pytest.fixture(scope="function")
def test_card() -> Card:
    simple_user = SimpleUser.objects.get_or_create(user_id=323, full_username="khorn")[0]
    # acc = test_bank_acc
    acc = BankingAccount.objects.get_or_create(account_number=100, account_owner=simple_user, currency_amount=500)[0]
    card = Card.objects.get_or_create(card_number=7777, MM=5, YY=2020, system="VISA", banking_account=acc)[0]
    return card


@pytest.fixture(scope="function")
def another_test_card() -> Card:
    simple_user = SimpleUser.objects.get_or_create(user_id=778, full_username="tzinch")[0]
    acc = another_test_bank_acc  # BankingAccount.objects.get_or_create(account_number=1, account_owner=simple_user, currency_amount=500)[0]
    card = Card.objects.get_or_create(card_number=8888, MM=5, YY=2020, system="VISA", banking_account=acc)[0]
    return card


@pytest.fixture(scope="function")
def another_test_bank_acc() -> BankingAccount:
    simple_user_2 = SimpleUser.objects.get_or_create(user_id=232, full_username="tzinch")[0]
    acc = BankingAccount.objects.get_or_create(account_number=9, account_owner=simple_user_2, currency_amount=500)[0]
    return acc



@pytest.fixture(scope="function")
def test_simple_user_for_handlers() -> SimpleUser:
    user = SimpleUser.objects.get_or_create(
        user_id=115,
        full_username="vortex",
        user_name="John",
        surname="Doe",
        phone_number=79506375555,
        friends=["Krigg"],
    )[0]
    return user

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

@pytest.fixture(scope="function")
def test_simple_bank_acc_with_user() -> BankingAccount:
    user = SimpleUser.objects.get_or_create(
        user_id=115,
        full_username="vortex",
        user_name="John",
        surname="Doe",
        phone_number=79506375555,
        friends=["Krigg"],
    )[0]
    acc = BankingAccount.objects.get_or_create(account_number=10, account_owner=user, currency_amount="25")[0]
    return acc

@pytest.fixture(scope="function")
def test_mock_bot():
    bot = MagicMock()
    return bot


##########################################
@pytest.fixture(scope="function")
def test_new_friend_message():
    user = SimpleUser.objects.get_or_create(
        user_id=112,
        full_username="vortex",
        user_name="John",
        surname="Doe",
        phone_number=79506376666,
        friends=["Krigg"],
    )[0]
    message = MagicMock()
    message.from_user = user
    message.from_user.id = 112
    message.text = "@Solanum"
    return message



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

#----#@@#@#@

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







# @pytest.fixture(scope="function")
# def transact_msg_1():
#     message = MagicMock()
#     message.text = "7777 2 5"
#     return message





# @pytest.fixture(scope="function")
# def test_simple_user() -> SimpleUser:
#     user = SimpleUser.objects.get_or_create(user_id=789, full_username="bloodgod")[0]
#     return user














































































































# @pytest.fixture(scope="function")
# def test_card_number():
#     return 7777
#
#
# @pytest.fixture(scope="function")
# def test_acc_number():
#     return 1






















































# @pytest.fixture(scope="function")
# def test_banking_account() -> BankingAccount:
#     acc = BankingAccount.objects.get_or_create(account_number=7, account_owner=789, currency_amount=500)[0]
#     return acc


#
# @pytest.fixture(scope="function")
# def test_card() -> Card:
#     simple_user_1 = SimpleUser.objects.get_or_create(user_id=256, full_username="tzinch")[0]
#     acc = BankingAccount.objects.get_or_create(account_number=56, account_owner=simple_user_1, currency_amount=500)[0]
#     card = Card.objects.get_or_create(card_number=7777, MM=5, YY=2020, system="VISA", banking_account=acc)[0]
#     return card

# @pytest.fixture(scope="function")
# def another_test_Card() -> Card:
#     simple_user_1 = SimpleUser.objects.get_or_create(user_id=257, full_username="khorn")[0]
#     acc = BankingAccount.objects.get_or_create(account_number=2, account_owner=simple_user_1, currency_amount=500)[0]
#     card = Card.objects.get_or_create(card_number=8888, MM=5, YY=2020, system="VISA", banking_account=acc)[0]
#     return card


# @pytest.fixture(scope="function")
# def test_bank_acc():
#     simple_user_1 = SimpleUser.objects.get_or_create(user_id=123, full_username="tzinch")[0]
#     acc = BankingAccount.objects.get_or_create(account_number=1, account_owner=simple_user_1, currency_amount=500)[0]
#     return acc


# @pytest.fixture(scope="function")
# def test_mock_message():
#     user = SimpleUser.objects.get_or_create(
#         user_id=112,
#         full_username="vortex2",
#         user_name="John",
#         surname="Doe",
#         phone_number=79506376666,
#         friends=["Krigg"],
#     )[0]
#     message = MagicMock()
#     message.from_user = user
#     message.from_user.id = 112
#     return message


# @pytest.fixture(scope="function")
# def test_bank_acc_rec() -> BankingAccount:
#     simple_user_2 = SimpleUser.objects.get_or_create(user_id=223, full_username="nurgle")[0]
#     acc = BankingAccount.objects.get_or_create(account_number=2, account_owner=simple_user_2, currency_amount=0)[0]
#     return acc



















# @pytest.fixture(scope="function")
# def test_simple_bank_acc_for_handlers_2() -> BankingAccount:
#     user = SimpleUser.objects.filter(user_id=115, full_username="Krigg", friends=["vortex"]).first()
#     acc = BankingAccount.objects.get_or_create(account_number=20, account_owner=user, currency_amount="0")[0]
#     return acc
#
#



# @pytest.fixture(scope="function")
# def test_mock_bot():
#     bot = MagicMock()
#     return bot


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
#                                                currency_amount=500)[0]
#     return acc


# @pytest.fixture(scope="function")
# def test_bank_acc() -> BankingAccount:
#     simple_user_1 = SimpleUser.objects.create(user_id=123, full_username="tzinch")
#     acc = BankingAccount.objects.create(account_number=1, account_owner=simple_user_1, currency_amount=500)
#     return acc










