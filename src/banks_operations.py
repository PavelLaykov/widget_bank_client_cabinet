import re
from collections import Counter


def search_operations(operations: list[dict], search: str) -> list[dict]:
    """
    Функция для поиска в списке словаре определенной операции по столбцу "description"
    :param operations: список словарей с операциями
    :param search: ключевые слова для поиска
    :return: список словарей с результатами поиска
    """
    if not operations or not search:
        return []
    result = []

    for operation in operations:
        description = operation.get("description", "")
        if isinstance(description, str):
            search_result = re.search(pattern=search, string=description, flags=re.I)
            if search_result:
                result.append(operation)

    return result


def banking_operations(data_operations: list[dict], categories: list) -> dict[str, int]:
    """
    Функция для создания словаря с типом банковской операции по входным данным,
    где ключ = названия категорий, а значение = количество операций
    :param data_operations: список словарей с данными о банковских операциях
    :param categories: список категорий операций
    :return: словарь (ключ = названия категорий, значение = количество операций)
    """
    if not data_operations or not categories:
        return {}
    found_categories = []

    for operation in data_operations:
        description = operation.get("description", "")
        for category in categories:
            if re.search(pattern=category, string=description, flags=re.IGNORECASE):
                found_categories.append(category)
    result = dict(Counter(found_categories))
    return result


if __name__ == "__main__":
    transactions = [
        {"id": 1, "amount": 1000, "currency": "RUB", "description": "Перевод с карты на карту"},
        {"id": 2, "amount": 2000, "currency": "USD", "description": "Перевод с карты на карту"},
        {"id": 3, "amount": 1500, "currency": "EUR", "description": "Открытие вклада"},
        {"id": 4, "amount": 500, "currency": "RUB", "description": "Открытие вклада"},
    ]
    searches = input("Введите тип искомой операции: ")
    tests_search = search_operations(transactions, searches)
    print(tests_search)

    # categories_list = ["Перевод с карты на карту", "Открытие вклада", "Оплата услуг", "Перевод организации"]
    # tests_search_list = banking_operations(transactions, categories_list)
    # print(tests_search_list)
