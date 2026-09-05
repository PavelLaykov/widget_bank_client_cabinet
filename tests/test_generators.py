import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# Тест def filter_by_currency в файле generators.py
def test_filter_by_currency(transactions: list) -> None:
    """Тест на корректный вывод данных по валюте (currency = USD)"""
    assert list(filter_by_currency(transactions, "USD")) == [
        {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "USD"}}, "description": "Payment"},
        {"id": 3, "operationAmount": {"amount": "150", "currency": {"code": "USD"}}, "description": "Refund"},
    ]


def test_filter_by_currency_no_currency(transactions: list) -> None:
    """Тест на отсутствие нужной валюты"""
    assert list(filter_by_currency(transactions, "RUB")) == ([])


def test_filter_by_currency_no_data() -> None:
    """Тест на передачу пустого списка"""
    assert list(filter_by_currency([], "USD")) == ([])


# Тесты для def transaction_descriptions в файле generators.py


def test_transaction_descriptions(transactions: list[dict]) -> None:
    """Тест на правильность описания каждой транзакции
    :type transactions: Список транзакций
    """
    result = list(transaction_descriptions(transactions))
    assert result == ["Payment", "Transfer", "Refund"]


def test_transaction_descriptions_no_data() -> None:
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (100001, 100002, ["0000 0000 0010 0001", "0000 0000 0010 0002"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list) -> None:
    """Тесты на генерацию карты"""
    assert card_number_generator(start, stop) == expected


@pytest.mark.parametrize("start, stop", [(0, 2), (2, 1), (1, 9999999999999999999)])
def test_card_number_generator_not_correct(start: int, stop: int) -> None:
    """Тест на неправильные вводимые данные"""
    with pytest.raises(ValueError) as er:
        card_number_generator(start, stop)
        assert str(er.value) == "Неправильные вводимые данные"


def test_card_number_generator_wrong_type() -> None:
    """Тест на неправильный тип данных"""
    with pytest.raises(TypeError) as er:
        card_number_generator("a", "b")  # type: ignore
        assert str(er.value) == "Некорректный номер"
