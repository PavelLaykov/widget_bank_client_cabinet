from typing import Dict, List, Any


def filter_by_state(list_of_dicts: List[Dict[str, Any]], state="EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""
    return [item for item in list_of_dicts if item.get("state") == state]


transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(filter_by_state(transactions, "EXECUTED"))


def sort_by_date(list_of_sort_date: List[Dict[str, Any]], descending=True) -> List[Dict[str, Any]]:
    """Функция должна возвращать новый список, отсортированный по дате (date)"""
    return sorted(list_of_sort_date, key=lambda x: x.get("date", ""), reverse=descending)


test_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(sort_by_date(test_date))
