from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('D:\GB Codes\Home Work Python 8\data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('D:\GB Codes\Home Work Python 8\data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('Вывожу данные для Вас данные из 1-ого файла\n')
    with open('D:\GB Codes\Home Work Python 8\data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        data_middle = ''
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    print('Вывожу данные для Вас данные из 2-ого файла\n')
    with open('D:\GB Codes\Home Work Python 8\data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second



def name_change():
    new_name = input("Введите новое имя: ")
    return new_name

def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        # Можно добавить проверку, чтобы человек не выходил за пределы записей

        # Предлагаем менять поля отдельно
        print(f'Изменить данную запись\n{data_first[number_journal]}')
        print('Какие данные Вы хотите изменить?')
        print('1 - Имя\n2 - Фамилия\n3 - Телефон\n4 - Адрес')
        field_number = int(input('Введите номер поля: '))

        if field_number == 1:
            new_name = name_change()
            old_data = data_first[number_journal].split('\n')
            old_data[0] = new_name
            new_data = '\n'.join(old_data) + '\n'
            data_first[number_journal] = new_data

        elif field_number == 2:
            new_surname = surname_data()
            old_data = data_first[number_journal].split('\n')
            old_data[1] = new_surname
            new_data = '\n'.join(old_data) + '\n'
            data_first[number_journal] = new_data

        elif field_number == 3:
            new_phone = phone_data()
            old_data = data_first[number_journal].split('\n')
            old_data[2] = new_phone
            new_data = '\n'.join(old_data) + '\n'
            data_first[number_journal] = new_data

        elif field_number == 4:
            new_address = address_data()
            old_data = data_first[number_journal].split('\n')
            old_data[3] = new_address
            new_data = '\n'.join(old_data) + '\n'
            data_first[number_journal] = new_data

        with open('D:\GB Codes\Home Work Python 8\data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')

    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        # Можно добавить проверку, чтобы человек не выходил за пределы записи

        # Предлагаем менять поля отдельно
        print(f'Изменить данную запись\n{data_second[number_journal]}')
        print('Какие данные Вы хотите изменить?')
        print('1 - Имя\n2 - Фамилия\n3 - Телефон\n4 - Адрес')
        field_number = int(input('Введите номер поля: '))

        if field_number == 1:
            new_name = name_change()
            old_data = data_second[number_journal].split(';')
            old_data[0] = new_name
            new_data = ';'.join(old_data) + '\n'
            data_second[number_journal] = new_data

        elif field_number == 2:
            new_surname = surname_data()
            old_data = data_second[number_journal].split(';')
            old_data[1] = new_surname
            new_data = ';'.join(old_data) + '\n'
            data_second[number_journal] = new_data

        elif field_number == 3:
            new_phone = phone_data()
            old_data = data_second[number_journal].split(';')
            old_data[2] = new_phone
            new_data = ';'.join(old_data) + '\n'
            data_second[number_journal] = new_data

        elif field_number == 4:
            new_address = address


def delete_single_data(filename, data):
    print(f'Удалить данную запись\n{data}')
    data_index = int(input('Введите номер записи: ')) - 1
    if data_index in range(len(data)):
        data.pop(data_index)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(''.join(data))
        print('Изменения успешно сохранены!')
    else:
        print('Неверный номер записи!')

def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))
    
    if number_file == 1:
        print(f'В файле {number_file} есть {len(data_first)} записей')
        delete_option = input('Вы хотите удалить отдельную запись? (Y/N)').upper()
        if delete_option == 'Y':
            delete_single_data('data_first_variant.csv', data_first)
        else:
            print("Какую именно запись по счету Вы хотите удалить?")
            number_journal = int(input('Введите номер записи: '))
            print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
            data_first = data_first[:number_journal - 1] + data_first[number_journal:]
            with open('D:\GB Codes\Home Work Python 8\data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(''.join(data_first))
            print('Изменения успешно сохранены!')
    else:
        print(f'В файле {number_file} есть {len(data_second)} записей')
        delete_option = input('Вы хотите удалить отдельную запись? (Y/N)').upper()
        if delete_option == 'Y':
            delete_single_data('data_second_variant.csv', data_second)
        else:
            print("Какую именно запись по счету Вы хотите удалить?")
            number_journal = int(input('Введите номер записи: '))
            print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
            data_second = data_second[:number_journal - 1] + data_second[number_journal:]
            with open('D:\GB Codes\Home Work Python 8\data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(''.join(data_second))
            print('Изменения успешно сохранены!')


