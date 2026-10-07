import datetime

from src.banks_operations import search_operations
from src.financial_operations import read_csv_transactions, read_excel_transactions
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transaction
from src.widget import mask_card_number


def main() -> None:
    """
    Функция для запуска всего проекта
    :return: возвращает данные по запросу пользователя в формате
    """

    # 1. Выбор формата файла
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    data = None
    while data is None:
        search_file = (
            input(
                """Выберите необходимый пункт меню:
                   1. Получить информацию о транзакциях из JSON-файла
                   2. Получить информацию о транзакциях из CSV-файла
                   3. Получить информацию о транзакциях из XLSX-файла\n"""
            )
            .strip()
        )
        if search_file == "1":
            print("Для обработки выбран JSON-файл")
            data = get_transaction("./data/operations.json")

        elif search_file == "2":
            print("Для обработки выбран CSV-файл")
            data = read_csv_transactions("./transactions.csv")

        elif search_file == "3":
            print("Для обработки выбран XLSX-файл")
            data = read_excel_transactions("./transactions_excel.xlsx")

        else:
            print(f"Введено неверное значение {search_file}")
            continue


    # 2. Фильтрация по статусу операции
    if data is None:
        print("Получены пустые данные")
        return

    filtered_data = None
    while filtered_data is None:
        operation_status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
            .strip()
        )

        if operation_status in ["EXECUTED", "CANCELED", "PENDING"]:
            filtered_data = filter_by_state(data, operation_status)  # type: ignore

        else:
            print(f"Статус операции {operation_status} недоступен ")
            continue

    # 3. Сортировка по дате
    sorted_data = None
    while sorted_data is None:
        sorting_data_input = input("Отсортировать операции по дате? Да/Нет\n").lower().strip()
        if sorting_data_input in ["да"]:
            while True:
                sort_ascending_descending = input("Отсортировать по возрастанию или по убыванию?\n").lower()
                if sort_ascending_descending in ["по возрастанию", "по убыванию"]:
                    if sort_ascending_descending == "по возрастанию":
                        sorted_data = sort_by_date(filtered_data, not descending)
                        break
                    elif sort_ascending_descending == "по убыванию":
                        sorted_data = sort_by_date(filtered_data, descending)
                        break
                else:
                    sorted_data = sort_by_date(filtered_data, descending)
                    print("Неправильно выбрана команда")
                    continue
        elif sorting_data_input in ["нет"]:
            sorted_data = filtered_data
            break
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'")
            continue

    # 4. Фильтрация по валюте (рубли)
    currency_data = None
    while currency_data is None:
        sorting_value = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
        if sorting_value in ["да"]:
            currency = "RUB"
            sorted_nominal = filter_by_currency(sorted_data, currency)
            sorted_nominal_list = list(sorted_nominal)
            if not sorted_nominal_list:
                print("Рублевых транзакций не найдено")
                currency_data = sorted_data
            else:
                currency_data = sorted_nominal_list
        elif sorting_value in ["нет"]:
            currency_data = sorted_data
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'")
            continue

    # 5. Фильтрация по ключевому слову
    final_data = None
    while final_data is None:
        sorting_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
        if sorting_by_word in ["да"]:
            input_keyword = input("Введите слово для поиска в описании: ").strip().lower()
            final_data = search_operations(currency_data, input_keyword)
            print(final_data)
        elif sorting_by_word in ["нет"]:
            final_data = currency_data
            print(final_data)
        else:
            print("Неправильно выбрана команда")
            continue

    # 6. Вывод результатов
    print(f"\nРаспечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(final_data)}\n")
    if len(final_data) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    for transaction in final_data:
        # Форматирование времени
        date_transaction = transaction["date"]
        try:
            date = datetime.datetime.strptime(date_transaction, "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            date = datetime.datetime.strptime(date_transaction, "%Y-%m-%dT%H:%M:%SZ")
        formatted_date = datetime.fromisoformat(date).strftime("%d.%m.%Y")
        print(f"{formatted_date} {transaction['description']}")

        # Получение и маскировка номеров карт и счетов
        transaction_number_card_to = str(transaction.get("to", ""))
        transaction_number_card_from = str(transaction.get("from", ""))

        transaction_to = transaction_number_card_to not in ["nan", "none", "", "<null>", "None"]
        transaction_from = transaction_number_card_from not in ["nan", "none", "", "<null>", "None"]

        if transaction_to and transaction_from:
            print(
                f"{mask_card_number(transaction_number_card_to)} "
                f"-> {mask_card_number(transaction_number_card_from)}"
            )
        elif transaction_to:
            print(f"{mask_card_number(transaction_number_card_to)}")

        # Вывод суммы транзакций

        try:
            print(f"Сумма: {transaction['amount']} {transaction["currency_code"]}\n")
        except KeyError:
            print(
                f"Сумма: {transaction['operationAmount']['amount']}"
                f" {transaction["operationAmount"]["currency"]["name"]}\n"
            )


if __name__ == "__main__":
    main()
