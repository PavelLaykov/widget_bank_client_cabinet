from unittest.mock import Mock, mock_open, patch

from src.financial_operations import read_csv_transactions, read_excel_transactions


def test_read_csv_transactions() -> None:
    """Функция тестирования чтения файла об операциях в формате .csv"""
    with patch("builtins.open", mock_open(read_data="id;state\n593027;CANCELED")):
        assert read_csv_transactions("") == [{"id": "593027", "state": "CANCELED"}]


@patch("pandas.read_excel")
def test_read_excel_transactions(mock_get: Mock) -> None:
    """Функция тестирования чтения файла об операциях в формате .xlsx"""
    mock_get.return_value.to_dict.return_value = [{"id": "593027", "state": "CANCELED"}]
    assert read_excel_transactions("") == [{"id": "593027", "state": "CANCELED"}]


def test_read_csv_transactions_errors() -> None:
    """Функция тестирования ошибки чтения файла об операциях в формате .csv"""
    assert read_csv_transactions("") == "Файл CSV не обнаружен или неверный формат файла"


def test_read_excel_transactions_errors() -> None:
    """Функция тестирования ошибки чтения файла об операциях в формате .xlsx"""
    assert read_excel_transactions("") == "Файл Excel не обнаружен или неверный формат файла"
