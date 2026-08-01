def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает маску номера карты клиента банка в формате XXXX XX** **** XXXX."""
    # Превращаем в строку, если пришло число
    card_number_str = str(card_number)
    # Формируем маску: первые 6 цифр, звезды и последние 4
    if len(card_number_str) != 16:
        return "Номер карты не верный"
    else:
        block_1 = card_number_str[:4]
        block_2 = card_number_str[4:6] + "**"
        block_3 = "****"
        block_4 = card_number_str[12:]
        masked_card = block_1 + " " + block_2 + " " + block_3 + " " + block_4
    return masked_card


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета в формате **XXXX."""
    account_number_str = str(account_number)
    if len(account_number_str) != 20:
        return "Номер счёта не верный"
    else:
        masked_account = f"**{account_number[-4:]}"
    return masked_account


# Пример использования:

print(get_mask_card_number("7000792289606361"))
# Вывод: 7000 79** **** 6361

print(get_mask_account("73654108430135874305"))
# Вывод; **4305
