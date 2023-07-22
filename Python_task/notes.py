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

def find_note(lst_notes: list) -> dict:
    search_criteria = input('Введите дату или заголовок заметки: ')
    for obj in lst_notes:
        for key, value in obj.items():
            if search_criteria.lower() in value.lower():
                return obj

def print_note(dic_note=False, lst_notes=False):
    if dic_note:
        print(f'{dic_note["heading"].upper()}\n{dic_note["text"]}')
    if lst_notes:
        lst_notes = sorted(lst_notes, key=lambda x: x['id-date'])
        for item in lst_notes:
            print(f'{item["heading"].upper()}\n{item["text"]}')

def change_note(lst_notes: list, change_note: dict) -> list:
    index_note = lst_notes.index(change_note)
    option = int(input('Введите поле изменения: 1 - заголовок, 2 - текс заметки. - '))
    if option == 1:
        change_note['heading'] = input('Введите новый заголовок: ')
    elif option == 2:
        change_note['text'] = input('Введите новый текст заметки: ')
    else: print('Неверная команда!')
    change_note['change_last_date'] = str(get_date())
    lst_notes[index_note] = change_note
    return lst_notes

def delete_note(lst_notes: list, change_note: dict) -> list:
    index_note = lst_notes.index(change_note)
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

if user_option == 1:
    list_notes = read_file(path_file)
    new_list_notes = add_note(list_notes)
    write_file(path_file, new_list_notes)
    print('Заметка успешно добавлена!')
elif user_option == 2:
    list_notes = read_file(path_file)
    most_wanted_note = find_note(list_notes)
    print_note(dic_note = most_wanted_note)
elif user_option == 3:
    list_notes = read_file(path_file)
    most_wanted_note = find_note(list_notes)
    new_list_notes = change_note(list_notes, most_wanted_note)
    write_file(path_file, new_list_notes)
    print('Заметка успешно изменена!')
elif user_option == 4:
    list_notes = read_file(path_file)
    most_wanted_note = find_note(list_notes)
    new_list_notes = delete_note(list_notes, most_wanted_note)
    write_file(path_file, new_list_notes)
    print('Заметка успешно удалена!')
elif user_option == 5:
    list_notes = read_file(path_file)
    print_note(lst_notes = list_notes)
else: print('Неправильный ввод команды!')