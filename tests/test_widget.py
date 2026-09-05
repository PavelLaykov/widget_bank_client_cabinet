import pytest

from src.widget import mask_card_number, get_date


# Тестирование файла src.masks функции mask_card_number
# Параметризация для def mask_card_number
@pytest.mark.parametrize(
    "input_card, output_card",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_card_number(input_card: str, output_card: str) -> None:
    """Тест на кодирование номера"""
    assert mask_card_number(input_card) == output_card


@pytest.mark.parametrize(
    "card_input",
    [
        "Visa Platinum 70007922896361",
        "Счет 646864736788979589",
        "",
        " ",
        "Visa Platinum hjdlghwtpbcdfgju",
        "Счет sss8647367889477958s",
    ],
)
def test_mask_card_number_error(card_input: str) -> None:
    """Тест на различные случаи невалидного ввода для маскировки номера карты"""
    with pytest.raises(ValueError):
        mask_card_number(card_input)


# Тест src/widget.py функции def get_date
# Параметризация для def get_date
@pytest.mark.parametrize(
    "input_date, out_data",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11T02:26:18", "11.03.2024"),
        ("2024-03-11T00:00:00", "11.03.2024"),
        ("2024-03-11T23:59:59.999999", "11.03.2024"),
        ("0001-01-01T00:00:00", "01.01.0001"),
        ("9999-12-31T23:59:59", "31.12.9999"),
        ("2024-03-11T02:26:18.123", "11.03.2024"),
        ("2024-03-11T02:26:18.1", "11.03.2024"),
    ],
)
def test_date_formats(input_date: str, out_data: str) -> None:
    """Тест различных форматов даты и времени"""
    assert get_date(input_date) == out_data


def test_basic_date_conversion() -> None:
    """Тест базового преобразования даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "no_date_string",
    [
        "",  # Пустая строка
        "   ",  # Пробелы
        "12:26:18",  # Только время
    ],
)
def test_strings_without_date(no_date_string: str) -> None:
    """Тест строк, где отсутствует дата"""
    with pytest.raises(ValueError):
        get_date(no_date_string)
