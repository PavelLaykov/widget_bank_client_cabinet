# Импортируем функции get_mask_card_number и get_mask_account из модуля masks.py
from masks import get_mask_card_number
from masks import get_mask_account

# Импорт модуля re
import re

# Импорт модуля datetime
from datetime import datetime

def mask_account_card(account_card: str) -> str:
    """ Маскирует полученный номер карты или счета.
    Принимает один аргумент — строку, содержащую тип и номер карты или
    номер счёта, и возвращает строку с замаскированным номером.
    Использует функции get_mask_card_number и get_mask_account из модуля masks. """
    # card_number - пример номера карты
    # account_number - пример номера счета

    if "Счёт" in account_card:  # Создается маска для счета
        letters_part = "".join(re.findall(r"\D+", account_card))
        numbers_part = "".join(re.findall(r"\d+", account_card))
        hidden_account_card = f"{letters_part} {get_mask_account(numbers_part)}"
    else:  # Создается маска для номера карты
        letters_part = "".join(re.findall(r"\D+", account_card))
        numbers_part = "".join(re.findall(r"\d+", account_card))
        hidden_account_card = f"{letters_part} {get_mask_card_number(numbers_part)}"

    return hidden_account_card


def get_date(date: str) -> str:
    """ Функция принимает на вход строку в формате "2026-07-27T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("27.07.2026").
    """
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date.strftime("%d.%m.%Y")
