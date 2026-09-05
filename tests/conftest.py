from typing import Dict, Any

import pytest

# ФИКСТУРЫ для файла masks.py

# Фикстура для test_get_mask_account_valid в masks.py
@pytest.fixture
def card_number() -> list[tuple[str, str]]:
    """Возвращает правильный номер карты (16 цифр)."""
    return [
        ("1111222233334444", "1111 22** **** 4444"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
    ]

# Фикстура для test_get_mask_account_valid_fixture в masks.py
@pytest.fixture
def account_number():
    """Возвращает правильный номер счета (20 цифр)."""
    return "12345678901234567890"

@pytest.fixture
def date_src():
    """Возвращает правильную дату в формате ISO."""
    return "2024-12-25"

@pytest.fixture
def sample_transactions():
    """Список транзакций для тестов filter_by_state и sort_by_date."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Фикстура для test_get_mask_account_valid_fixture в masks.py
@pytest.fixture
def mask_account() -> list[tuple[str, str]]:
    return [("73654108430135874305", "**4305"), ("12345678901234567890", "**7890"), ("11111222225555588888", "**8888")]


@pytest.fixture
def mask_card_number() -> list[tuple[str, str]]:
    return [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ]


@pytest.fixture
def account_number() -> list[tuple[str, str]]:
    return [("73654108430135874305", "**4305"), ("12345678901234567890", "**7890"), ("11111222225555588888", "**8888")]


# Тесты для processing.py функции def filter_by_state


@pytest.fixture
def executed_state_data() -> list[Dict[str, Any]]:
    """Фикстура только с EXECUTED операциями"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def same_date_data() -> list[Dict[str, Any]]:
    """Фикстура с одинаковыми датами"""
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_operation() -> list[Dict[str, Any]]:
    """Фикстура для filter_by_state в файле processing.py"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-15T12:30:45.123456", "amount": 100.50},
        {"id": 4, "state": "EXECUTED", "date": "2023-10-12T18:20:15.321654", "amount": 75.25},
        {"id": 6, "state": "EXECUTED", "date": "2023-10-10T11:30:05.654321", "amount": 150.00},
        {"id": 8, "state": "EXECUTED", "date": "2023-10-08T13:15:20.456123", "amount": 200.00},
    ]

# Фикстуры для файла generators.py
@pytest.fixture
def sort_data_operation() -> list[dict[str, Any]]:
    """Фикстура sort_by_date в файле processing.py"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def transactions() -> list[dict[str, Any]]:
    """Фикстура для filter_by_currency, transaction_descriptions в файле generators.py"""
    return [
        {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "USD"}}, "description": "Payment"},
        {"id": 2, "operationAmount": {"amount": "200", "currency": {"code": "EUR"}}, "description": "Transfer"},
        {"id": 3, "operationAmount": {"amount": "150", "currency": {"code": "USD"}}, "description": "Refund"},
    ]
