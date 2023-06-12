import os.path
from utils.func import format_date, is_account, is_card, mask_number_account, mask_number_card, get_data

file = os.path.join("..", "operations.json")

if __name__ == "__main__":
    # Получаем данные из файла operations.json
    operations = get_data(file)

    # Сортируем список по ключу 'date' по убыванию.
    operations.sort(key=lambda d: d.get("date", '0'), reverse=True)

    # Запускаем цикл по списку словарей, выводя на печать значения по ключам
    # вводим счетчик для подсчета напечатанных позиций, при достижении счетчика - 5, прерываем цикл
    counter = 0
    for operation in operations:
        # Выводим на печать только операции со статусом "Исполнено"
        if operation.get('state') == 'EXECUTED':
            # Выводим отформатированную дату операции
            print(format_date(operation.get("date", 0)), end=' ')
            # Выводим описание операции
            print(operation.get('description'))
            # Выводим номера счета и/или карты в замаскированном формате
            if is_account(operation.get('from')):
                print(f"{mask_number_account(operation.get('from'))} ->", end=' ')
            if is_card(operation.get('from')):
                print(f"{mask_number_card(operation.get('from'))} ->", end=' ')
            if is_account(operation.get('to')):
                print(mask_number_account(operation.get('to')))
            if is_card(operation.get('to')):
                print(mask_number_card(operation.get('to')))
            # Выводим сумму и валюту операции
            print(operation['operationAmount']['amount'], end=' ')
            print(operation['operationAmount']['currency']['name'])
            print()
            # Увеличиваем счетчик, при достижении 5 прерываем
            counter += 1
            if counter == 5:
                break
