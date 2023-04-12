import pytest

from app.internal.services.banking_service \
    import get_card_by_id, get_acc_by_user, get_acc_by_id

# Создать тестового юзера и тестоую карту

# Получение карты по номеру карты
# получение акка по номеру акка
# получение акка по id юзера !!!!! (всех)

# update телефона
# создание юзера
# получение юзера по юзернейму
# получение юзера по ид


# ТРАНЗАКЦИИ(3 типа)


@pytest.mark.django_db
def test_get_card_by_number_ok(test_card_number, test_card):
    card = get_card_by_id(test_card_number)
    assert card == test_card

@pytest.mark.django_db
def test_get_acc_by_acc_number_ok(test_acc_number, test_bank_acc):
    acc = get_acc_by_id(test_acc_number)
    assert acc == test_bank_acc


