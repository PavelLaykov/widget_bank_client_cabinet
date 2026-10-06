import json
from typing import Any
from unittest.mock import Mock, mock_open, patch

import requests
from more_itertools import side_effect

from src.external_api import currency_conversion, transactions_sum
from src.utils import get_transaction


def test_currency_conversion(transactions: Mock):
    """Тестирование функции конвертации валюты"""
    with patch("builtins.open", mock_open(read_data=json.dumps(transactions))):
        with patch("requests.get") as mock_requests:
            with patch("os.path.exists") as mock_path_exists:
                mock_path_exists.return_value = True
                mock_requests.return_value.status_code = 200
                mock_requests.return_value.json.return_value = {"result": 0}
                assert transactions_sum(" ") == 100


@patch('src.external_api.requests.get')
def test_currency_conversion_success(mock_get: Any) -> None:
    """Тестирование на успешную конвертацию валюты с ожидаемым результатом"""
    mock_response = Mock()
    mock_response.json.return_value = {'result': 74.5}
    mock_get.return_value = mock_response

    transaction = {
        'operationAmount': {
            'amount': '1',
            'currency': {
                'code': 'USD'
            }
        }
    }

    # Вызов тестируемой функции
    result = currency_conversion(transaction)

    # Проверка результата
    assert result == 74.5


# Тест на ошибку HTTP
@patch('src.external_api.requests.get')
def test_currency_conversion_status(mock_get: Mock):
    """Тест на определение данных транзакции"""
    transaction = {
        'operationAmount': {
            'currency': {'code': 'USD'},
            'amount': '100'
        }
    }

    # Имитация ошибки HTTP
    mock_response = mock_get.return_value
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Mocked HTTP error")

    # Проверка, что функция возвращает None
    result = currency_conversion(transaction)
    assert result is None

    # Убедиться, что raise_for_status был вызван
    mock_get.return_value.raise_for_status.assert_called_once()


@patch('src.external_api.requests.get')
def test_key_error_handling(mock_get: Any) -> None:
    """Тестирование на неправильный формат ответа"""

    # Имитация ответа API с отсутствующим ключом 'result'
    mock_get.return_value.json.return_value = {}
    mock_get.return_value.status_code = 200

    # Данные транзакции без нужного ключа
    transaction = {
        'operationAmount': {
            'currency': {'code': 'USD'},
            'amount': '100'
        }
    }

    try:
        currency_conversion(transaction)
    except KeyError:
        print('KeyError caught as expected')


@patch("builtins.open", side_effect=json.JSONDecodeError("123", "321", 1))
def test_decode_error(mock_open: Mock):
    """Тестирование на выброс ошибки при пустом словаре"""
    assert get_transaction(" ") == []
    with patch("os.path.exists") as mock_path_exists:
        mock_open.rereturn_value = True
        mock_path_exists.return_value = True
        assert get_transaction(" ") == []



@patch("builtins.open", side_effect=Exception)
def test_decode_error_exception(mock_file: Mock):
    """Тест, если файл повреждён"""
    assert get_transaction(" ") == []
    with patch("os.path.exists") as mock_path_exists:
        mock_file.return_value = True
        mock_path_exists.return_value = True
        assert get_transaction(" ") == []
