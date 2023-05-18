import datetime

import phonenumbers
import telebot
from django.db import transaction as transaction_locker

from app.internal.models.banking_account import BankingAccount
from app.internal.models.transaction import Transaction
from app.internal.services import banking_service
from app.internal.transport.bot.text_serialization_handlers import convert_dict_to_str
from app.internal.transport.information_former import form_information_handlers
from app.internal.transport.messages import common_messages
from app.internal.users.application import user_service
from app.internal.users.db_data.models import AuthUser, SimpleUser
from app.internal.users.domain.services import get_hash_from_password


def error_handler(exc, message, bot):
    bot.send_message(message.chat.id, common_messages.MESSAGE_DICT.get("error_send_message") + f" {exc}")


def error_decorator(orig_func):
    def wrapper(*args, **kwargs):
        try:
            orig_func(*args, **kwargs)
        except Exception as exc:
            error_handler(exc, args[0], args[1])

    return wrapper


def access_decorator(orig_func):
    def wrapper(*args, **kwargs):
        bot = args[1]
        message = args[0]
        user = user_service.get_user_by_id(args[0].from_user.id)
        if user.login_access:
            orig_func(*args, **kwargs)
        else:
            bot.send_message(message.chat.id, "access restricted")

    return wrapper


@error_decorator
def help_handler(message: telebot.types.Message, bot):
    bot.send_message(message.chat.id, common_messages.help_command_message())


@access_decorator
@error_decorator
def currency_amount_handler(message: telebot.types.Message, bot):
    msg = bot.send_message(message.chat.id, common_messages.ask_for_card_acc_number())
    bot.register_next_step_handler(msg, send_amount_inf, bot)


def send_amount_inf(message: telebot.types.Message, bot):
    user_inf = form_information_handlers.get_user_information(message.from_user.id)
    if user_inf is None:
        bot.send_message(message.chat.id, common_messages.no_information_in_db_message)
        return
    try:
        amount = form_information_handlers.get_currency_information(user_inf, int(message.text))
    except PermissionError:
        bot.send_message(message.chat.id, common_messages.access_denied())
        return
    if amount is not None:
        bot.send_message(message.chat.id, amount)
    else:
        bot.register_next_step_handler(
            bot.send_message(message.chat.id, common_messages.no_card_or_acc()), send_amount_inf, bot
        )


@access_decorator
@error_decorator
def me_inf_handler(message: telebot.types.Message, bot):
    bot.send_message(
        message.chat.id, convert_dict_to_str(form_information_handlers.get_user_information(message.from_user.id))
    )


@error_decorator
def start_handler(message: telebot.types.Message, bot):
    user = message.from_user
    password = "123"
    default_updates = {"user_name": user.first_name, "surname": user.last_name, "full_username": user.username}
    auth_user = user_service.create_auth_user(user.id, password)
    # bot.send_message(message.chat.id, "@@@")
    # bot.send_message(message.chat.id, user.id)
    auth_user_obj = AuthUser.objects.filter(username=auth_user.get["username"]).first()
    user_service.update_create_user(user.id, default_updates, auth_user_obj)

    bot.send_message(message.chat.id, common_messages.user_add_message(user.username))


@access_decorator
@error_decorator
def phone_number_handler(message: telebot.types.Message, bot):
    msg = bot.send_message(message.chat.id, common_messages.ask_for_phone_number_message())
    bot.register_next_step_handler(msg, get_phone_number, bot)


def get_phone_number(message: telebot.types.Message, bot):
    if phonenumbers.is_valid_number(phonenumbers.parse(message.text, "IN")):
        number = int(message.text)
        user_service.update_user_number(message.from_user.id, number)
        bot.send_message(message.chat.id, common_messages.add_phone_number_message(message.from_user.username))
    else:
        msg = bot.send_message(message.chat.id, common_messages.incorrect_phone_number_message())
        bot.register_next_step_handler(msg, get_phone_number, bot)


@access_decorator
@error_decorator
def my_money_recipient(message: telebot.types.Message, bot):
    user = user_service.get_user_by_id(message.from_user.id)
    if user is None:
        bot.send_message(message.chat.id, common_messages.no_information_in_db_message)
        return
    spec_users = list(user.friends.all())
    if len(spec_users) == 0:
        bot.send_message(message.chat.id, "No users in money-friends_list")
        return
    msg = ""
    for user in spec_users:
        msg += user.full_username + "\n"
    bot.send_message(message.chat.id, "This is your money-friends list:")
    bot.send_message(message.chat.id, msg)


@access_decorator
@error_decorator
def add_money_recipient(message: telebot.types.Message, bot):
    msg = bot.send_message(message.chat.id, common_messages.ask_for_user_name())
    bot.register_next_step_handler(msg, add_user, bot)


def add_user(message: telebot.types.Message, bot):
    if message.text[0] != "@" or len(message.text.split()) != 1:
        answer = bot.send_message(message.chat.id, common_messages.incorrect_user_name())
        bot.register_next_step_handler(answer, add_user, bot)
    else:
        user = user_service.get_user_by_id(message.from_user.id)
        if user is None:
            return
        another_user = user_service.get_user_by_username(message.text[1:])
        if another_user is None:
            pass
        else:
            user.friends.add(another_user)
            bot.send_message(message.chat.id, "Successful add user to money-friends")


@access_decorator
@error_decorator
def delete_money_recipient(message: telebot.types.Message, bot):
    msg = bot.send_message(message.chat.id, common_messages.ask_for_user_name())
    bot.register_next_step_handler(msg, remove_user, bot)


def remove_user(message: telebot.types.Message, bot):
    if message.text[0] != "@" or len(message.text.split()) != 1:
        answer = bot.send_message(message.chat.id, common_messages.incorrect_user_name())
        bot.register_next_step_handler(answer, remove_user, bot)
    else:
        user = user_service.get_user_by_id(message.from_user.id)
        if user is None:
            return
        another_user = user_service.get_user_by_username(message.text[1:])
        if another_user is None:
            pass
        else:
            user.friends.remove(another_user)
            bot.send_message(message.chat.id, "Successful delete user from money-friends")


@access_decorator
@error_decorator
def make_transaction(message: telebot.types.Message, bot):
    msg = bot.send_message(
        message.chat.id,
        "enter the transfer way you choose: \n" "by username: 1\n by card_number: 2\n" "by bank_acc number: 3",
    )
    bot.register_next_step_handler(msg, ask_for_requisites, bot)


def ask_for_requisites(message: telebot.types.Message, bot):
    msg = bot.send_message(
        message.chat.id,
        "enter your card number, then card number/bank acc/ username of another user and amount of money to transfer",
    )
    func_dict = {"1": "username_transaction", "2": "card_transaction", "3": "bank_acc_transaction"}
    if message.text in func_dict.keys():
        bot.register_next_step_handler(msg, get_data_and_transact_2, bot, message.text)
    else:
        bot.send_message(message.chat.id, "incorrect input")


def safe_get_bank_accounts_id(reqs, message_text):
    our_acc = banking_service.get_card_by_id(int(reqs[0])).banking_account
    if message_text == "1":
        another_user = user_service.get_user_by_username(reqs[1])  # !
        if another_user is None:
            raise ValueError("пользователь не найден в БД")
        another_bank_acc_id = (
            BankingAccount.objects.filter(account_owner=another_user).values_list("account_number", flat=True).first()
        )
    elif message_text == "2":
        another_card = banking_service.get_card_by_id(int(reqs[1]))  # !
        if another_card is None:
            raise ValueError("карта с таким номером не найдена в БД")
        another_bank_acc_id = another_card.banking_account.account_number
    elif message_text == "3":
        another_bank_acc = banking_service.get_acc_by_id(int(reqs[1]))  # !
        if another_bank_acc is None:
            raise ValueError("банковский счет получателя с такими реквизитами отсутствует")
        another_bank_acc_id = another_bank_acc.account_number
    else:
        raise ValueError("Некорректный тип перевода")
    return our_acc.account_number, another_bank_acc_id, our_acc.currency_amount


def get_data_and_transact_2(message: telebot.types.Message, bot, message_text: str):
    reqs = message.text.split()
    if not incorrect_reqs(reqs[0], reqs[1], reqs[2], message_text) or len(reqs) != 3:
        bot.send_message(message.chat.id, "incorrect data")
        return
    amount = int(reqs[2])
    bank_acc_id, another_bank_acc_id, our_money = safe_get_bank_accounts_id(reqs, message_text)

    bot.send_message(message.chat.id, str(bank_acc_id) + str(another_bank_acc_id))

    if send_msg_if_not_enough_money(bot, message.chat.id, amount, our_money):
        return
    safe_transaction(amount, bank_acc_id, another_bank_acc_id, bot, message.chat.id)
    confirm_transaction(bot, message.chat.id)


def safe_transaction(amount, our_acc_number, other_acc_number, bot, chat):
    bot.send_message(chat, "@")

    with transaction_locker.atomic():
        BankingAccount.objects.select_for_update().get(pk=1)
        our_bank = BankingAccount.objects.select_for_update().get(account_number=our_acc_number)
        our_bank.currency_amount -= amount
        our_bank.save()
        other_bank = BankingAccount.objects.select_for_update().get(account_number=other_acc_number)
        other_bank.currency_amount += amount
        other_bank.save()
        Transaction.objects.create(
            transaction_recipient=other_bank.account_owner,
            transaction_sender=our_bank.account_owner,
            amount=amount,
            transaction_date=datetime.date.today(),
        )
    bot.send_message(chat, "@##@#")


# def get_data_and_transact(message: telebot.types.Message, bot, message_text: str):
#     reqs = message.text.split()
#     if not incorrect_reqs(reqs[0], reqs[1], reqs[2], message_text) or len(reqs) != 3:
#         bot.send_message(message.chat.id, "incorrect data")
#         return
#     amount = int(reqs[2])
#     with transaction_locker.atomic():
#         try:
#             bank_acc, another_bank_acc = get_bank_accounts(reqs, message_text)
#             transaction(bot, message, amount, bank_acc, another_bank_acc)
#         except ValueError as error:
#             bot.send_message(message.chat.id, error)


# def get_acc_numbers(reqs, message_text):
#     if message_text == "1":
#         another_user_name = reqs[1]
#         another_user = user_service.get_user_by_username(another_user_name)  # !
#         if another_user is None:
#             raise ValueError("пользователь не найден в БД")
#         another_bank_acc_number = banking_service.get_acc_by_user(another_user.user_id)


# def get_bank_accounts(reqs, message_text):
#     bank_acc = banking_service.get_card_by_id(int(reqs[0])).banking_account  # !
#     if message_text == "1":
#         another_user_name = reqs[1]
#         another_user = user_service.get_user_by_username(another_user_name)  # !
#         if another_user is None:
#             raise ValueError("пользователь не найден в БД")
#         another_bank_acc = banking_service.get_acc_by_user(another_user.user_id)  # !
#     elif message_text == "2":
#         another_card_number = int(reqs[1])
#         another_card = banking_service.get_card_by_id(another_card_number)  # !
#         if another_card is None:
#             raise ValueError("карта с таким номером не найдена в БД")
#         another_bank_acc = another_card.banking_account
#     elif message_text == "3":
#         another_bank_acc_number = int(reqs[1])
#         another_bank_acc = banking_service.get_acc_by_id(another_bank_acc_number)  # !
#     else:
#         another_bank_acc = bank_acc
#     if another_bank_acc is None:
#         raise ValueError("банковский счет получателя с такими реквизитами отсутствует")
#     if bank_acc is None:
#         raise ValueError("номер вашей карты введен неправильно")
#     return bank_acc, another_bank_acc


# def transaction(
#         bot, message: telebot.types.Message, amount: int, bank_acc: BankingAccount, another_bank_acc: BankingAccount
# ):
#     if send_msg_if_not_enough_money(bot, message.chat.id, amount, bank_acc.currency_amount):
#         return
#
#     bank_acc.currency_amount -= amount  # !
#     bank_acc.save()
#     another_bank_acc.currency_amount += amount  # !
#     another_bank_acc.save()
#     transaction_date = datetime.date.today()
#     Transaction.objects.create(
#         transaction_recipient=another_bank_acc.account_owner,
#         transaction_sender=bank_acc.account_owner,
#         amount=amount,
#         transaction_date=transaction_date,
#     )
#     confirm_transaction(bot, message.chat.id)


def incorrect_reqs(user_cart: str, main_req: str, amount: str, code: str):
    return user_cart.isdigit() and amount.isdigit() and (main_req.isdigit() or (not main_req.isdigit() and code == "1"))


def send_msg_if_not_enough_money(bot, msg_id, transaction_amount, acc_amount):
    if transaction_amount <= 0 or acc_amount - transaction_amount < 0:
        bot.send_message(msg_id, "not enough money or incorrect amount. Transaction will be cancelled")
        return True
    return False


def confirm_transaction(bot, msg_id):
    bot.send_message(msg_id, "transaction confirmed")


@error_decorator
def new_password_handler(message: telebot.types.Message, bot):
    if user_service.get_user_by_id(message.from_user.id).hash_of_password is None:
        msg = bot.send_message(message.chat.id, "У вас отсутствует пароль. Введите новый пароль")
        bot.register_next_step_handler(msg, change_password, bot)
    else:
        msg = bot.send_message(message.chat.id, "Введите текущий пароль")
        bot.register_next_step_handler(msg, verify_current_password_bot, bot)


def verify_current_password_bot(message: telebot.types.Message, bot):
    if get_hash_from_password(message.text) == user_service.get_user_by_id(message.from_user.id).hash_of_password:
        msg = bot.send_message(message.chat.id, "Введите новый пароль")
        bot.register_next_step_handler(msg, change_password, bot)
    else:
        bot.send_message(message.chat.id, "Пароль неверный. Отказано в доступе.")


def change_password(message: telebot.types.Message, bot):
    user_service.update_user_password(message.from_user.id, message.text)
    bot.send_message(message.chat.id, "Пароль успешно изменён.")


def add_rights(user: SimpleUser):
    user.login_access = True


@access_decorator
@error_decorator
def get_full_log(message: telebot.types.Message, bot):
    user = user_service.get_user_by_id(message.from_user.id)
    sender_logs = list(Transaction.objects.filter(transaction_recipient=user))
    recipient_logs = list(Transaction.objects.filter(transaction_sender=user))
    # logs = list(user.transactions_history.all())
    res_list = ["исходящие переводы:\n"]

    for el in sender_logs:
        res_list.append(
            f"получатель: {el.transaction_recipient.full_username}\n"
            f"сумма: {el.amount}\n"
            f"дата: {el.transaction_date}\n"
            # f"{'снятие' if el.is_outgoing_transaction == True else 'пополнение'}\n"
            f"######\n"
        )
    res_list.append("$$$$$$")
    res_list.append("входящие переводы:\n")
    for el in recipient_logs:
        res_list.append(
            f"отправитель: {el.transaction_sender.full_username}\n"
            f"сумма: {el.amount}\n"
            f"дата: {el.transaction_date}\n"
            # f"{'снятие' if el.is_outgoing_transaction == True else 'пополнение'}\n"
            f"######\n"
        )
    res_list.append("$$$$$$")

    bot.send_message(message.chat.id, result_handler(res_list))


@access_decorator
@error_decorator
def all_transaction_recipients(message: telebot.types.Message, bot):
    user = user_service.get_user_by_id(message.from_user.id)
    res_list = []
    senders = set()
    recipients = set()

    # MB Distinct

    # !!!!!! Values_list вернет просто идентификатор
    for el in list(Transaction.objects.filter(transaction_recipient=user)):
        senders.add(el.transaction_sender)

    for el in list(Transaction.objects.filter(transaction_sender=user)):
        recipients.add(el.transaction_recipient)

    bot.send_message(message.chat.id, recipients)

    for uniq_sender in senders:
        res_list.append(f"отправитель: {uniq_sender.full_username}\n")
    res_list.append("############\n")
    for uniq_recipient in recipients:
        res_list.append(f"получатель: {uniq_recipient.full_username}\n")
    bot.send_message(message.chat.id, result_handler(res_list))


def result_handler(res_list):
    res = "".join(res_list)
    return res if len(res) > 0 else "your transaction history is empty"


# @error_decorator
# def login_handler(message: telebot.types.Message, bot):
#     user = user_service.get_user_by_id(message.from_user.id)
#     if user.hash_of_password is None:
#         bot.send_message(message.chat.id, "У вас отсутствует пароль. Воспользуйтесь командой /new_password")
#         return
#     else:
#         access_token = AuthToken.objects.filter(user=user, token_type="access")
#         refresh_token = AuthToken.objects.filter(user=user, token_type="refresh")
#         if len(list(access_token)) == 0 and len(list(refresh_token)) == 0:
#             msg = bot.send_message(message.chat.id, "Введите свой пароль")
#             bot.register_next_step_handler(msg, check_password, bot)
#         elif token_service.check_is_expired(access_token.first()):
#             if refresh_token is None or token_service.check_is_expired(refresh_token.first()):
#                 token_service.revoke_all_tokens_for_user(user)
#                 bot.send_message(message.chat.id, "please, login again")
#                 return
#             else:
#                 token_service.update_and_get_tokens(user)
#         add_rights(user)
#         user.save()
#         bot.send_message(message.chat.id, "login was confirmed")
#
#
# def check_password(message: telebot.types.Message, bot):
#     user = user_service.get_user_by_id(message.from_user.id)
#     if len(message.text) > 0 and password_service.get_hash_from_password(message.text) == user.hash_of_password:
#         token_service.update_and_get_tokens(user)
#         add_rights(user)
#     else:
#         bot.send_message(message.chat.id, "ваш пароль не верный")
#
#
# def remove_rights(user: SimpleUser):
#     user.login_access = False
#
#
# @error_decorator
# def logout_handler(message: telebot.types.Message, bot):
#     user = user_service.get_user_by_id(message.from_user.id)
#     remove_rights(user)
#     user.save()
#     bot.send_message(message.chat.id, "logout was confirmed")
