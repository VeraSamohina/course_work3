from datetime import datetime
import json


def get_data(filename):
    """Получает json файл и конвертирует в объект Python"""
    raw_json = open(filename, encoding='utf-8')
    return json.load(raw_json)


def is_account(account):
    """
    :param account: строка, содержащая информацию о счете
    :return: True если строка не None и содержит слово "Счет", в обратном случае - False
    """
    if account is None:
        return False
    if "Счет" not in account:
        return False
    return True


def is_card(card):
    """
        :param card: строка, содержащая информацию о карте
        :return: True если строка не None и НЕ содержит слово "Счет", в обратном случае - False
        """
    if card is None:
        return False
    if "Счет" in card:
        return False
    return True


def mask_number_card(card):
    """
    Функция выводит строку с замаскированным номером карты в формате 7000 79** **** 6361
    :param card: строка с информацией о наименовании и номере карты
    :return: f-строка - наименование карты и замаскированный номер карты
    """
    card_list = card.split(' ')
    card_name = ' '. join(card_list[:-1])
    number_card = card_list[-1]
    number = list(number_card)
    for i in range(6, 12):
        number[i] = '*'
    number.insert(4, ' ')
    number.insert(9, ' ')
    number.insert(14, ' ')
    return f"{card_name} {''.join(number)}"


def mask_number_account(account):
    """
       Функция выводит строку с замаскированным номером счета в формате **9638
       :param account: строка с информацией о наименовании и номере карты
       :return: f-строка - слово "Счет" и замаскированный номер счета
       """
    account_list = account.split(' ')
    account_name = ' '. join(account_list[:-1])
    number_account = account_list[-1]
    number = list(number_account)
    number[0:14] = []
    number[0] = number[1] = '*'
    return f"{account_name} {''.join(number)}"


def format_date(date):
    """
    Функция получает строку с информацией о дате и переводит ее в необходимый формат
    :param date: дата (строка) в формате 2019-08-26T10:50:58.294041
    :return: дата (строка) в формате 26.08.2019
    """
    short_date = date[:10]
    return datetime.strptime(short_date, '%Y-%m-%d').strftime('%d.%m.%Y')
