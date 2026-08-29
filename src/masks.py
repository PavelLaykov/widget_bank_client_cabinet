def get_mask_card_number(card_number: str) -> str:
    """Функция получает номер карты пользователя и возвращает замаскированный номер"""

    try:
        card_number = card_number.replace(" ", "")
        if len(card_number) != 16 or not card_number.isdigit():
            raise ValueError(f"Номер карты должен содержать 16 цифр. Получено {len(card_number)}")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    except ValueError as e:
        return f"Ошибка: {e}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета и выводит его маску"""

    try:
        account_number = account_number.replace(" ", "")
        if len(account_number) != 20 or not account_number.isdigit():
            raise ValueError(f"Номер счета должен содержать 20 цифр. Получено {len(account_number)}")
        return f"**{account_number[-4:]}"

    except ValueError as e:
        return f"Ошибка: {e}"
