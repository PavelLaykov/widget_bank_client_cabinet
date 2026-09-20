import os

import requests
from dotenv import load_dotenv

from src.utils import get_transaction

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


def transactions_sum(file: str) -> float:
    """Принимает транзакции и возвращает их по валюте"""
    transactions_list = get_transaction(file)
    total_sum_rub = 0

    for i, transaction in enumerate(transactions_list):
        total_sum_rub += currency_conversion(transaction)
    return total_sum_rub


def currency_conversion(transaction) -> float:
    """Конвертирование валюты в рубли"""
    headers = {"apikey": API_KEY}

    code = transaction.get("operationAmount", {}).get("currency", {}).get("code", "")
    amount = transaction.get("operationAmount", {}).get("amount", 0)
    if code == "RUB":
        return round((float(transaction["operationAmount"]["amount"])), 2)

    rate_eur = requests.get(
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}",
        headers=headers,
        timeout=20,
    )

    if rate_eur.status_code == 200:
        result = dict(rate_eur.json()).get("result", 0)
        return round((float(result)), 2)
    else:
        return 0


if __name__ == "__main__":
    sum_rub = transactions_sum(file="data/operations.json")

    print(f'Итого:{sum_rub}рублей')
