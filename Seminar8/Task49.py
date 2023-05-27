# Задача №49. Решение в группах. Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def show_menu() -> int:
    print('\nВыберите необходимое действие:\n'
          '1. Отобразить весь справочник\n'
          '2. Найти абонента по фамилии\n'
          '3. Найти абонента по номеру телефона\n'
          '4. Добавить абонента в справочник\n'
          '5. Сохранить справочник в текстовом формате\n'
          '6. Законьчить работу\n')
    return int(input(' Введите номер пункта меню: '))

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('file.txt')

    while choice != 6:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_txt('file.txt', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        choice = show_menu()

def read_txt(filename: str) -> list:
    spr = []
    filds = ['Фамилия','Имя','Телефон','Описание']
    with open(filename, 'r', encoding='utf8') as data:
        for line in data:
            zap = dict(zip(filds, line.strip().split(',')))
            spr.append(zap)
    return spr

def write_txt(filename: str, data, list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for j in data[i].values():
                s += j + ','
            fout.write(f'{s[:-1]}\n')

def print_result(spr):
    print(*spr[0].keys())
    for i in range(len(spr)):
        s = ''
        for j in spr[i].values():
            s += j + '   ' + '\t'
            # s += '%-15s' % j
        print(f'{s[:-1]}')

def get_search_name():
    return input('\nВведите фамилию: ')

def find_by_name(spr, name):
    return next((x for x in spr if x['Фамилия'] == name), 'Не найдено')

def get_search_number():
    return input('\nВведите номер телефона: ')

def find_by_number(spr, number):
    return next((x for x in spr if x['Телефон'] == number), 'Не найдено')

def get_new_user():
    newuser = []
    newuser.append(input('\nВведите Фамилию: '))
    newuser.append(input('\nВведите Имя: '))
    newuser.append(input('\nВведите Телефон: '))
    newuser.append(input('\nВведите Описание: '))
    return newuser

def add_user(spr, user, data):
    filds = ['Фамилия','Имя','Телефон','Описание']
    zap = dict(zip(filds, user, data))
    spr.append(zap)

def get_file_name():
    return input('Укажите имя файла: ') + '.txt'

work_with_phonebook()

