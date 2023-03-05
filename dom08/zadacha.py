# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import os
os.system('clear')

def scan_base():
    base = open ('List.txt', 'r', encoding='utf-8')
    base_list = base.read()
    base.close()
    print(base_list)
    return base_list

def find_base():
    base = open ('List.txt', 'r', encoding='utf-8')
    data_in_base = base.read().split('\n')
    base.close()
    for i in range (len(data_in_base)):
        data_in_base[i] = data_in_base[i].split(' ')
    data = str(input('Введите данные для поиска: '))
    data_check = False
    for i in range (len(data_in_base)):
        for j in data_in_base [i]:
            if str(data).lower() == j.lower(): 
                data = data_in_base[i]
                data_check = True
    if data_check: print(f'Нашлись следующие данные {data}')
    else: print('Контакт не найден')

def add_base():
    base = open ('List.txt', 'a', encoding='utf-8')
    new_data = input('Введите данные нового сотрудника: ')
    base.write(f'\n{new_data}')
    base.close()
    print(new_data + ' успешно добавлен')


def delete_base():
    print('Для удаления данных необходимо получить права администратора')
    base = open('List.txt', 'r+', encoding='utf-8')
    data_in_list = base.read().split('\n')
    base.close()

def edit_base():
    print('Для редактирования необходимо получить права администратора')

def intro_text():
    print('Меню: ')
    print('1) Просмотреть весь справочник') 
    print('2) Найти контакт')
    print('3) Добавить новый контакт')
    print('4) Изменить данные контакта')
    print('5) Удалить контакт')
    
def menu(command):
    if command == 1:
        scan_base()
    elif command == 2:
        find_base()
    elif command == 3:
        add_base()
    elif command == 4:
        edit_base()
    elif command == 5:
        delete_base()

    else:
        os.system('clear')
        print('Пожалуйста, уточните действие')
        intro_text()
        menu(int(input('Выберите цифру соответствующую действию: ')))
    
base_list = ()
intro_text()

menu(int(input('Выберите цифру соответствующую действию: ')))
