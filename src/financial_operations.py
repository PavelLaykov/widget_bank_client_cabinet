import csv
from typing import Any

import pandas as pd


def read_csv_transactions(filename_csv: str) -> list[Any] | str:
    """
    Функция считывания CSV файла возвращает список словарей,
    :param filename_csv: передаётся файл CSV
    :return: список словарей
    """
    transactions_csv_return = []
    try:
        with open(filename_csv, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                transactions_csv_return.append(row)
        return transactions_csv_return
    except FileNotFoundError:
        return "Файл CSV не обнаружен или неверный формат файла"
    except Exception as e:
        return f"Ошибка при чтении CSV файла: {str(e)}"


def read_excel_transactions(filename_excel: str) -> list[Any] | str:
    """
    Функция считывания Excel файла возвращает список словарей,
    :param filename_excel: Excel файл
    :return: список словарей операций из файла Excel
    """
    try:
        reader = pd.read_excel(filename_excel)
        return reader.to_dict("records")
    except FileNotFoundError:
        return "Файл Excel не обнаружен или неверный формат файла"


if __name__ == "__main__":
    transactions_csv = read_csv_transactions("../transactions.csv")

    # if isinstance(transactions_csv, str):
    #     print(f"Ошибка: {transactions_csv}")
    # else:
    #     print(f"\n{'=' * 80}")
    #     print(f"НАЙДЕНО ТРАНЗАКЦИЙ: {len(transactions_csv)}")
    #     print(f"{'=' * 80}")
    #
    #     for i, transaction in enumerate(transactions_csv, 1):
    #         print(f"\n📋 ТРАНЗАКЦИЯ #{i}")
    #         for key, value in transaction.items():
    #             print(f"   {key}: {value}")
    #         print(f"   {'─' * 50}")

    transactions_excel = read_excel_transactions("../transactions_excel.xlsx")

    print(transactions_excel)
    print(f"НАЙДЕНО ТРАНЗАКЦИЙ: {len(transactions_excel)}")
    print(transactions_csv)
    print(f"НАЙДЕНО ТРАНЗАКЦИЙ: {len(transactions_csv)}")
