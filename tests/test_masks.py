from typing import Any

from src.masks import get_mask_card_number, get_mask_account


# Тестирование файла src.masks функции get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1111222233334444", "1111 22** **** 4444"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("9999888877776666", "9999 88** **** 6666"),
    ],
)
def test_get_mask_card_number_multiple(card_number: str, expected: str) -> None:
    """Тест на кодирование номера с несколькими случаями"""
    assert get_mask_card_number(card_number) == expected


# Тест для КАРТ файла src.masks функции get_mask_card_number
def test_get_mask_card_valid(card_number: list[tuple[str, str]]) -> None:
    for card_num, expected in card_number:
        assert get_mask_card_number(card_num) == expected


@pytest.mark.parametrize(
    "invalid_input, expected_exception",
    [
        ("11112222333344", ValueError),  # 14 цифр
        ("1", ValueError),  # 1 цифра
        ("111122223333444455", ValueError),  # 18 цифр
        ("", ValueError),
        (" ", ValueError),
        ("    ", ValueError),
        ("abcdefghijklmnop", ValueError),  # буквы
        ("1234abcd5678efgh", ValueError),  # цифры и буквы
        ("!@#$%^&*()_+{}|:", ValueError),  # символы
        ("1111-2222-3333-4444", ValueError),  # с дефисами
    ],
)
def test_get_mask_card_number_invalid(invalid_input: str, expected_exception: Exception) -> None:
    """Тест на ValueError"""
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_input)


# Тестирование файла src.masks функции get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
        ("11111222225555588888", "**8888"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    """Тест на корректное кодирование валидных номеров счетов"""
    assert get_mask_account(int(account_number)) == expected


# Тест для СЧЕТОВ файла src.masks функции get_mask_card_number
def test_get_mask_account_valid(account_number: list[tuple[str, str]]) -> None:
    for account_num, expected in account_number:
        assert get_mask_account(int(account_num)) == expected


def test_get_mask_account_valid_fixture(mask_account: list[tuple[str, str]]) -> None:
    """Тест с ФИКСТУРАМИ на корректное кодирование номеров счетов"""
    for card_number, expected in mask_account:
        assert get_mask_account(int(card_number)) == expected


@pytest.mark.parametrize(
    "invalid_account_number",
    [
        "736541084301358743",  # 18 цифр
        "1234567890",  # 10 цифр
        "1",  # 1 цифра
        "",  # пустая строка
        " ",  # пробел
        "     ",  # 5 пробелов
        "abcdefghijklmnop",  # буквы
        "1234abcd5678efgh",  # цифры и буквы
        "!@#$%^&*()_+{}|:",  # символы
    ],
)
def test_get_mask_account_invalid(invalid_account_number: str) -> None:
    """Тест на обработку невалидных номеров счетов"""
    with pytest.raises(ValueError):
        get_mask_account(int(invalid_account_number))


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
