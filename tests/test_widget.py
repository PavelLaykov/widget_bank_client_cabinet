from typing import Any

import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card_visa(card_number: Any) -> None:
    """Проверяем, что функция правильно маскирует карту VISA."""
    result = mask_account_card(f"Visa {card_number}")
    assert result == "Visa 1234 56** **** 3456"


def test_mask_account_card_mastercard(card_number: Any) -> None:
    """Проверяем, что функция правильно маскирует карту Mastercard."""
    result = mask_account_card(f"Mastercard {card_number}")
    assert result == "Mastercard 1234 56** **** 3456"


def test_mask_account_card_account(account_number: Any) -> None:
    """Проверяем маскировку счета."""
    result = mask_account_card(f"Счет {account_number}")
    assert result == "Счет **7890"


def test_mask_account_card_with_spaces() -> None:
    """Проверяем обработку номера с пробелами."""
    result = mask_account_card("Visa 1234567890123456")
    assert result == "Visa 1234 56** **** 3456"


@pytest.mark.parametrize("card_type", ["Visa", "Mastercard", "Мир"])
def test_all_cards(card_type: Any, card_number: Any) -> None:
    """Параметризованный тест: проверяем маскировку разных типов карт."""
    result = mask_account_card(f"{card_type} {card_number}")
    assert "****" in result


def test_mask_account_card_error_short() -> None:
    """Проверяем ошибку при коротком номере."""
    result = mask_account_card("Visa 1234567890")
    assert "Ошибка" in result or "Существует" in result


def test_mask_account_card_error_empty() -> None:
    """Проверяет ошибку при пустой строке."""
    result = mask_account_card("")
    assert "Ошибка" in result or "существует" in result


def test_get_date_normal(date_src: Any) -> None:
    """Проверяет преобразование обычной даты."""
    result = get_date(date_src)
    assert result == "25.12.2024"


def test_get_date_with_time(date_src: Any) -> None:
    """Проверяет преобразование даты с временем."""
    result = get_date(f"{date_src}T15:30:00")
    assert result == "25.12.2024"


def test_get_date_error_empty() -> None:
    """Проверяет ошибку при пустой строке."""
    with pytest.raises(Exception):
        get_date("")


@pytest.mark.parametrize(
    "invalid_date",
    [
        "",
        "25.12.2024",
        "2024-13-01",
        "2024-02-30",
        "привет мир",
    ],
)
def test_get_date_errors(invalid_date: Any) -> None:
    """Параметризованный тест: проверяет ошибки при неверных форматах даты."""
    with pytest.raises(Exception):
        get_date(invalid_date)
