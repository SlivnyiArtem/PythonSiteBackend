import pytest

from app.internal.services.banking_service import get_card_by_id

# Создать тестового юзера и тестоую карту

# Получение карты по номеру карты
# получение акка по номеру акка
# получение акка по id юзера !!!!! (всех)

# update телефона
# создание юзера
# получение юзера по юзернейму
# получение юзера по ид


# ТРАНЗАКЦИИ


@pytest.mark.django_db
def test_get_card_by_number_ok(test_card_number, test_card):
    card = get_card_by_id(test_card_number)
    assert card == test_card
