from src.masks import get_mask_account, get_mask_card_number


def hidden_account_card(card_number: str, account_number: str) -> str:
    # card_number - пример номера карты
    # пример номера счета

    masked_card = get_mask_card_number(card_number)
    masked_account = get_mask_account(account_number)

    return f"Маскированный номер карты: {masked_card} \n Маскированный номер счета: {masked_account}"


if __name__ == "__main__":
    #main("7000792289606361", "73654108430135874305")
    hidden_account_card("Visa Platinum 7000792289606361", "Счёт 73654108430135874305")
"""
Примеры входных данных для проверки функции
Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305
"""
