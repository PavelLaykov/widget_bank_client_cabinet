from datetime import datetime

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    """Функция обрабатывает информацию о картах и о счетах. Возвращает тип и замаскированный номер"""
    try:
        if not account_card or account_card.strip() == "":
            raise ValueError("Пустая строка")

        list_info = account_card.split()

        if len(list_info) < 2:
            raise ValueError("Нужно вести тип и номер карты или счета")

        card_type = " ".join(list_info[:-1])
        number = list_info[-1]
        number = number.replace(" ", "").replace("-", "")

        if not number.isdigit():
            raise ValueError("Номер должен содержать только цифры")

        if len(number) == 16:
            masked = get_mask_card_number(number)
            return f"{card_type} {masked}"
        elif len(number) == 20:
            masked = get_mask_account(number)
            return f"{card_type} {masked}"
        else:
            raise ValueError(f"Длина номера {len(number)}. Нужно 16, либо 20")

    except ValueError as e:
        return f"Ошибка: {e}"


def get_date(date_now: str) -> str:
    """Функция принимает на вход строку с датой в одном формате и возвращает строку в другом формате"""
    date_format = datetime.fromisoformat(date_now)
    return date_format.strftime("%d.%m.%Y")

