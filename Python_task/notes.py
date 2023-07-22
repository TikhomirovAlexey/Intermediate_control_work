path_file = 'notes.json'
import json
import datetime

def get_date() -> datetime:
    dt_now = datetime.datetime.now()
    return dt_now

def read_file(path: str) -> list:
    with open(path, 'r', encoding='UTF-8') as read_file:
        data = json.load(read_file)
    return data

def add_note(lst_notes: list) -> list:
    obj = {}
    obj['id-date'] = str(get_date())
    obj['heading'] = input('Введите заголовок заметки: ')
    obj['text'] = input('Введите содержание заметки: ')
    lst_notes.append(obj)
    return lst_notes

def find_note(lst_notes: list) -> list:
    search_criteria = input('Введите дату или заголовок заметки: ')
    list_find_notes = []
    for obj in lst_notes:
        for key, value in obj.items():
            if search_criteria.lower() in value.lower():
                list_find_notes.append(obj)
    return list_find_notes

def print_note(lst_notes):
        lst_notes = sorted(lst_notes, key=lambda x: x['id-date'], reverse=True)
        for item in lst_notes:
            print(f'{item["heading"].upper()}\n{item["text"]}\n')

def change_note(lst_notes: list, change_note: list) -> list:
    for item in change_note:
        index_note = lst_notes.index(item)
        option = int(input('Введите поле изменения: 1 - заголовок, 2 - текс заметки. - '))
        if option == 1:
            item['heading'] = input('Введите новый заголовок: ')
        elif option == 2:
            item['text'] = input('Введите новый текст заметки: ')
        else: print('Неверная команда!')
        item['change_last_date'] = str(get_date())
        lst_notes[index_note] = item
    return lst_notes

def delete_note(lst_notes: list, change_note: list) -> list:
    for item in change_note:
        index_note = lst_notes.index(item)
        tmp_option = int(input('Вы действительно хотите удалить заметку? 1 - да, 2 - нет.'))
        if tmp_option == 1:
            del lst_notes[index_note]
        elif tmp_option == 2:
            print('Отмена действия!')
        else: print('Неверная команда!')
    return lst_notes

def write_file(path: str, new_lst: list):
    with open(path, 'w', encoding='UTF-8') as write_file:
        json.dump(new_lst, write_file, ensure_ascii=False, indent=2)



user_option = int(input('Введите команду: 1 - новая заметка, 2 - показать заметку, 3 - редактировать заметку, 4 - удалить заметку, 5 - показать все заметки. - '))
list_notes = read_file(path_file)

if user_option == 1:
    new_list_notes = add_note(list_notes)
    write_file(path_file, new_list_notes)
    print('Заметка успешно добавлена!')
elif user_option == 2:
    most_wanted_note = find_note(list_notes)
    if len(most_wanted_note) > 0:
        print_note(most_wanted_note)
    else: print('Такой заметки нет!')
elif user_option == 3:
    most_wanted_note = find_note(list_notes)
    if len(most_wanted_note) > 0:
        print_note(most_wanted_note)
        new_list_notes = change_note(list_notes, most_wanted_note)
        write_file(path_file, new_list_notes)
        print('Заметка успешно изменена!')
    else: print('Такой заметки нет!')
elif user_option == 4:
    most_wanted_note = find_note(list_notes)
    if len(most_wanted_note) > 0:
        new_list_notes = delete_note(list_notes, most_wanted_note)
        write_file(path_file, new_list_notes)
        print('Заметка успешно удалена!')
    else: print('Такой заметки нет!')
elif user_option == 5:
    print_note(list_notes)
else: print('Неправильный ввод команды!')