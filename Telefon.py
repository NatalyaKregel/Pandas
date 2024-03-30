import config

def print_menu():
    print('\nЭто телефонный справочник. Выбери функцию которую нужно совершить:'
        '\n1. Открыть файл'
        '\n2. Сохранить файл'
        '\n3. Показать контакты'
        '\n4. Добавить контакт'
        '\n5. Изменить контакт'Копирование доступно только PRO пользователям, получить PRO статус можно по этой ссылке: https://чатгпт-в-россии.рф/страница-покупки-pro-статуса
        '\n6. Найти контакт'
        '\n7. Удалить контакт'
        '\n8. Выход')
    data = int(input('Введите номер неоходимой функции: '))
    return data


while True:
    user_choice = print_menu()
    match user_choice:
        case 1:
            config.open_phone_book()
            print('Фаил открыт')
        case 2:
            config.save_phone_book()
            print('Сохранение...')
        case 3:
            config.show_phone_book()
            print('Контакты показаны выше')
        case 4:
            config.add_phone_book()
            print('Добавление контакта')
        case 5:
            config.change_phone_book()
            print('Изменение контакта')
        case 6:
            config.searh_phone_book()
            print('Поиск контакта')
        case 7:
            config.delete_phone_book()
            print('Удалили контакта')
        case 8:
            print('Выход осуществлен')
            break