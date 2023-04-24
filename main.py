import json
import datetime

def read_notes_file(): # Функция для чтения списка заметок из файла
    try:
        with open('notes.json', 'r', encoding='utf8') as f:
            notes = json.load(f)
    except BaseException as e:
        notes = []
    return notes


def save_notes_json(notes):  # Функция для сохранения списка заметок в файл
    with open('notes.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(notes, indent=4, default=str))
        # json.dump(notes, f, indent=4, ensure_ascii=False, sort_keys=False, default=str)
        # json.dump(notes, f, indent=4)


def print_notes(notes): # Функция для вывода выбранной записи или всего списка заметок
    if not notes:
        print('Заметок не найдено')
        print('---') 
    else:
        for note in notes:
            print(f'ID: {note["id"]}')
            print(f'Заголовок: {note["title"]}')
            print(f'Текст заметки: {note["body"]}')
            print(f'Дата/время: {note["timestamp"]}')
            print('---')        


def add_note(notes): # Функция для добавления новой заметки
    max_id = 0
    for item in notes:
        if item['id'] > max_id:
            max_id = item['id']
    id = max_id + 1      
    title = input('Введите заголовок: ')
    body = input('Введите текст заметки: ')
    timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    new_note = {'id': id, 'title': title, 'body': body, 'timestamp': timestamp}
    notes.append(new_note)
    return notes


def edit_note(notes, id): # Функция для редактирования заметки
        for note in notes:
            count = 0                       
            if note['id'] == id:
                count = 1            
                new_title = input(f'Введите новый заголовок (было: {note["title"]}): ')
                new_body = input(f'Введите новое тело заметки (было: {note["body"]}): ')
                note['title'] = new_title
                note['body'] = new_body
                note['timestamp'] = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                print(f'Заметка №{id} отредактирована')
                break
        if count == 0: print('Заметка с таким ID не найдена')    
        return notes


def filter_by_date(notes, date): # Функция для фильтрации заметок по дате
    filtered_notes = []
    for note in notes:
        note_date = datetime.datetime.strptime(note['timestamp'], '%d-%m-%Y %H:%M:%S')
        if note_date.date() == date:
            filtered_notes.append(note)
    return filtered_notes
    # print_notes(filtered_notes)


def delete_note_by_id(notes, id): # Функция для удаления заметки по номеру
    for index, note in enumerate(notes):
        if note['id'] == id:
            del notes[index]
    return notes
    # save_notes_json(notes)
    # print(f'Заметка №{id} удалена')


def delete_note_by_title(notes, title): # Функция для удаления заметки по заголовку
    for index, note in enumerate(notes):
        if note['title'] == title:
            del notes[index]
    return notes
    # save_notes_json(notes)
    # print(f'Заметка удалена')


def main():  # Функция главного меню
    
    # file_name = "notes.json"
    notes = read_notes_file()

    while True:
        print('Выберите действие:')
        print('1. Вывести все заметки')
        print('2. Вывести заметки за определенную дату')
        print('3. Вывести конкретную заметку')
        print('4. Добавить новую заметку')
        print('5. Редактировать заметку')
        print('6. Удалить заметку по номеру')
        print('7. Удалить заметку по заголовку')
        print('8. Выход')

        choice = input('Ваш выбор: ')
        print('---') 

        if choice == '1':
            print_notes(notes)

        elif choice == '2':
            date_str = input('Введите дату в формате ДД-ММ-ГГГГ: ')
            date = datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
            # filter_by_date(notes, date)
            filtered_notes = filter_by_date(notes, date)
            print_notes(filtered_notes)

        elif choice == '3':
            id = int(input('Введите ID заметки: '))
            note = [note for note in notes if note['id'] == id]
            print_notes(note)
            
        elif choice == '4':
            notes = add_note(notes)
            save_notes_json(notes)
            print('Заметка успешно добавлена')
            print('---') 

        elif choice == '5':
            id = int(input('Введите ID заметки для редактирования: '))            
            notes = edit_note(notes, id)
            save_notes_json(notes)                        
            print('---')            

        elif choice == '6':
            id = int(input('Введите ID заметки для удаления: '))
            notes = delete_note_by_id(notes, id)
            save_notes_json(notes)
            print(f'Заметка №{id} удалена')
            print('---')

        elif choice == '7':
            title = input('Введите заголовок заметки для удаления: ')
            notes = delete_note_by_title(notes, title)
            save_notes_json(notes)
            print(f'Заметка удалена')
            print('---')  

        elif choice == '8':
            break

        else:
            print('Неверный выбор пункта меню')
            print('---') 


if __name__ == '__main__':
    main()