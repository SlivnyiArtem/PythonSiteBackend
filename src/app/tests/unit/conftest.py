import pytest

from app.internal.models.banking_card import Card


@pytest.fixture(scope="function")
def test_card_1(test_bank_acc_1) -> Card:
    return Card.objects.get_or_create(card_number=7777, MM=5, YY=2020, system="VISA", banking_account=test_bank_acc_1)[
        0
    ]


@pytest.fixture(scope="function")
def test_card_2(test_bank_acc_2) -> Card:
    return Card.objects.get_or_create(card_number=8888, MM=5, YY=2020, system="VISA", banking_account=test_bank_acc_2)[
        0
    ]
