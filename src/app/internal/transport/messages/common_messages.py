MESSAGE_DICT = {
    "error_send_message": "при отправке сообщения возникла ошибка: ",
    404: "К сожалению, в базе данных о "
    "Вас нет информации. Попробуйте "
    "добавить себя в неё через команду бота /start",
    403: "В доступе к комманде отказано. " "Введите свой номер с помощью комманды /set_phone",
}


def user_add_message(name: str):
    return f"пользователь {name} успешно " f"добавлен в базу данных, либо данные о нём обновлены"


def ask_for_phone_number_message():
    return "Укажите номер телефона, " "который вы хотите добавить в базу"


def add_phone_number_message(name: str):
    return f"Телефонный номер успешно " f"добавлен к данным пользователя {name}"


def incorrect_phone_number_message():
    return "Некорректный номер, проверьте " "правильность формата, затем введите ещё раз"


def no_information_in_db_message():
    return (
        "К сожалению, в базе данных о "
        "Вас нет информации. Попробуйте "
        "добавить себя в неё через команду бота /start"
    )


def access_restricted_message():
    return "В доступе к комманде отказано. " "Введите свой номер с помощью комманды /set_phone"


def help_command_message():
    return (
        "Для сохранения информации о себе "
        "в базе данных введите команду /start"
        "для добавления номера телефона "
        "используйте команду /set_phone"
        "команда /me вывыедет сохраненную "
        "в БД информацию о вашем текущем пользователе"
        "команда /help (которой вы уже "
        "воспользовались) предоставит краткую справку."
        "Чтобы получить данные о количестве денег на счете,"
        " используйте команду /check_currency. "
        "Слава Омниссии!!! Ave Deus Mechanicus!!! ##18"
    )


def ask_for_card_acc_number():
    return "Введите номер карты или счета"


def no_card_or_acc():
    return (
        "Не существует карты или счета "
        "с таким привязанным номером,"
        " привязанным к вашему пользователю, "
        "проверьте правильность "
        "счета и повторите ввод"
    )


def access_denied():
    return "Доступ к данному аккаунту запрещен, вы не являетесь его владельцем"


def ask_for_user_name():
    return "Введите имя пользователя"


def incorrect_user_name():
    return "Некорректное имя пользователя повторите ввод"
