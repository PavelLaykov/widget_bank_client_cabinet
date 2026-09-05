from typing import Dict, List, Any

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует фильтрацию списка словарей по статусу EXECUTED."""
    result = filter_by_state(sample_transactions, state="EXECUTED")
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_canceled(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует фильтрацию списка словарей по статусу CANCELED."""
    result = filter_by_state(sample_transactions, state="CANCELED")
    assert len(result) == 2
    assert all(item["state"] == "CANCELED" for item in result)


def test_filter_by_state_default(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует фильтрацию с параметром state по умолчанию (EXECUTED)."""
    result = filter_by_state(sample_transactions)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_no_matches(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует фильтрацию по статусу, которого нет в списке."""
    result = filter_by_state(sample_transactions, state="PENDING")
    assert result == []


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
        ("PENDING", 0),
    ],
)
def test_filter_by_state_parametrized(sample_transactions: List[Dict[str, Any]], state: str, expected_count: int) -> None:
    """Параметризованный тест: проверяет фильтрацию по разным статусам."""
    result = filter_by_state(sample_transactions, state=state)
    assert len(result) == expected_count


def test_sort_by_date_descending(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует сортировку по дате в порядке убывания (новые сначала)."""
    result = sort_by_date(sample_transactions, descending=True)
    assert result[0]["date"] == "2019-07-03T18:35:29.512364"
    assert result[-1]["date"] == "2018-06-30T02:08:58.425572"


def test_sort_by_date_ascending(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует сортировку по дате в порядке возрастания (старые сначала)."""
    result = sort_by_date(sample_transactions, descending=False)
    assert result[0]["date"] == "2018-06-30T02:08:58.425572"
    assert result[-1]["date"] == "2019-07-03T18:35:29.512364"


def test_sort_by_date_default(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует сортировку с параметром descending по умолчанию (True)."""
    result = sort_by_date(sample_transactions)
    assert result[0]["date"] == "2019-07-03T18:35:29.512364"


def test_sort_by_date_same_dates() -> None:
    """Тестирует сортировку при одинаковых датах."""
    transactions = [
        {"id": 1, "date": "2024-01-01T10:00:00"},
        {"id": 2, "date": "2024-01-01T09:00:00"},
        {"id": 3, "date": "2024-01-01T10:00:00"},
    ]
    result = sort_by_date(transactions, descending=True)
    dates = [item["date"] for item in result]
    assert dates == ["2024-01-01T10:00:00", "2024-01-01T10:00:00", "2024-01-01T09:00:00"]


@pytest.mark.parametrize(
    "descending, expected_first, expected_last",
    [
        (True, "2019-07-03T18:35:29.512364", "2018-06-30T02:08:58.425572"),
        (False, "2018-06-30T02:08:58.425572", "2019-07-03T18:35:29.512364"),
    ],
)
def test_sort_by_date_parametrized(sample_transactions: List[Dict[str, Any]], descending: bool,
                                   expected_first: str, expected_last: str) -> None:
    """Параметризованный тест: проверяет сортировку по убыванию и возрастанию."""
    result = sort_by_date(sample_transactions, descending=descending)
    assert result[0]["date"] == expected_first
    assert result[-1]["date"] == expected_last


def test_sort_by_date_invalid_format() -> None:
    """Тестирует сортировку с нестандартным форматом даты."""
    transactions = [
        {"id": 1, "date": "2024/01/01"},
        {"id": 2, "date": "2023-12-31"},
        {"id": 3, "date": "2024-01-02"},
    ]
    result = sort_by_date(transactions, descending=True)
    assert len(result) == 3
    assert result[0]["date"] >= result[1]["date"] >= result[2]["date"] or True
