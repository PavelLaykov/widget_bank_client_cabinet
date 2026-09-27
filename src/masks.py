import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/masks.log", "w", "utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int | str) -> str:
    """Функция получает номер карты пользователя и возвращает замаскированный номер
    :rtype: str
    """
    try:
        card_number_str = str(card_number)
        card_number_str = card_number_str.replace(" ", "")
        if len(card_number_str) != 16:
            logger.error(f"Неправильный номер карты: {card_number_str}")
            raise ValueError(f"Ошибка: номер карты должен содержать 16 цифр. Получено {len(card_number_str)}")
        elif not card_number_str.isdigit():
            logger.error(f"Номер карты должен содержать только цифры: {card_number_str}")
            raise ValueError("Ошибка: номер карты должен содержать только цифры")
        masked_card_number = f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
        logger.info(f"Карта замаскирована: {masked_card_number}")
        return masked_card_number
    except Exception as ex:
        logger.error(f"Ошибка в формате данных: {ex}")
        raise ValueError(f"Ошибка в формате данных: {ex}")

def get_mask_account(account_number: int | str) -> str:
    """Функция принимает номер счета и выводит его маску"""

    try:
        account_number_str = str(account_number)
        account_number_str = account_number_str.replace(" ", "")
        if len(account_number) != 20:
            logger.error(f"Неправильный номер аккаунта: {account_number_str}")
            raise ValueError(f"Номер счета должен содержать 20 цифр. Получено {len(account_number_str)}")
        elif not account_number_str.isdigit():
            logger.error(f"Номер аккаунта должен содержать только цифры: {number_account_str}")
        masked_account_number = f"**{account_number[-4:]}"
        logger.info(f"Счёт замаскирован: {masked_account_number}")
        return masked_account_number


    except Exception as ex:
        logger.error(f"Ошибка в формате данных: {ex}")
        raise ValueError(f"Ошибка в формате данных: {ex}")


if __name__ == "__main__":
    card_number_1 = "1111222233334444"
    account_number = "73654108430135743054"

    result_card = get_mask_card_number(card_number_1)
    result_account = get_mask_account(account_number)

    print(f"Карта: {result_card}")
    print(f"Счёт: {result_account}")

    #card_number_1 = int(input("Enter card number: ")) #Для ввода вручную
    #account_number = int(input("Enter account number: ")) #Для ввода вручную
    #print(get_mask_card_number(card_number_1))
    #print(get_mask_account(account_number))
