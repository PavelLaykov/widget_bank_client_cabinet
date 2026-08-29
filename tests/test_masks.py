from typing import Any

from src.masks import get_mask_card_number, get_mask_account


def test_card_normal(card_number: Any) -> None:
    """Тестирует правильность маскировки номера карты."""

    result = get_mask_card_number(card_number)
    assert result == "1234 56** **** 3456"


def test_card_with_spaces() -> None:
    """Тестирует маскировку номера карты с пробелами."""

    result = get_mask_card_number("1234 5678 9012 3456")
    assert result == "1234 56** **** 3456"


def test_card_short() -> None:
    """Тестирует обработку короткого номера карты (<16 цифр)."""

    result = get_mask_card_number("1234567890")
    assert "Ошибка" in result


def test_card_empty() -> None:
    """Тестирует обработку пустой строки для номера карты."""

    result = get_mask_card_number("")
    assert "Ошибка" in result


def test_account_normal(account_number: Any) -> None:
    """Тестирует правильность маскировки номера счета."""

    result = get_mask_account(account_number)
    assert result == "**7890"


def test_account_short() -> None:
    """Тестирует обработку короткого номера счета (<20 цифр)"""

    result = get_mask_account("1234567890")
    assert "Ошибка" in result


def test_account_empty() -> None:
    """Тестирует обработку пустой строки для номера счета."""

    result = get_mask_account("")
    assert "Ошибка" in result
