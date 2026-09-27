import json
import logging
import os
from typing import Dict, List, Any

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/utils.log", "w", "utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def filter_by_state(list_of_dicts: List[Dict[str, Any]], state="EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению, по умолчанию "EXECUTED"."""

    return [item for item in list_of_dicts if item.get("state") == state]


transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
logger.info(f"Информация отфильтрована по названию страны и записана")
print(filter_by_state(transactions, "EXECUTED"))


def sort_by_date(list_of_sort_date: List[Dict[str, Any]], descending=True) -> List[Dict[str, Any]]:
    """Функция должна возвращать новый список, отсортированный по дате (date)"""
    logger.info(f"Информация отсортирована по дате и записана")
    return sorted(list_of_sort_date, key=lambda x: x.get("date", ""), reverse=descending)


def get_transaction(file: str) -> list[Any] | bool | Any:
    """Функция принимает файл JSON и возвращает список словарей"""
    file_exist = os.path.exists(file)
    if not file_exist:
        logger.error(f"Файл {file} не найден")
        return []
    try:
        with open(file, "r", encoding="utf-8") as transaction:
            transaction = json.load(transaction)
            if not isinstance(transaction, list):
                logger.error(f"Файл {file} не является списком")
                return []
            logger.info(f"Файл {file} открылся и информация записана")
            return transaction
    except json.JSONDecodeError:
        ex = "Что-то не так...(С файлом или его содержимым)"
        logger.error(f"Ошибка декодирования в {file}, ошибка: {ex}")
        print(ex)
        return []


if __name__ == "__main__":

    test_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    test_1 = filter_by_state(test_date, state="CANCELED")
    print(test_1)

    result = get_transaction(file="../data/operations.json")
    print(result)
