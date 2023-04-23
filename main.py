import json
import datetime


def read_notes_file(file_name):  # Функция для чтения списка заметок из файла
    with open(file_name, 'r') as data:
        try:
            notes = json.load(data)
            return notes
        except BaseException as e:
            print('The file contains invalid JSON')


def save_notes_json(notes, file_name):  # Функция для сохранения списка заметок в файл
    with open(file_name, 'w') as f:
        json.dump(notes, f, indent=4, ensure_ascii=False, sort_keys=False, default=str)


def print_notes(notes): # Функция для вывода выбранной записи или всего списка заметок
    if not notes:
        print('Заметок не найдено')
    else:
        for note in notes:
            print(f'ID: {note["id"]}')
            print(f'Заголовок: {note["title"]}')
            print(f'Текст заметки: {note["body"]}')
            print(f'Дата/время: {note["timestamp"]}')
            print('---')        


def add_note(notes): # Функция для добавления новой заметки
    id = len(notes) + 1
    title = input('Введите заголовок: ')
    body = input('Введите текст заметки: ')
    timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    new_note = {'id': id, 'title': title, 'body': body, 'timestamp': timestamp}
    notes.append(new_note)
    return notes


def filter_by_date(notes, date): # Функция для фильтрации заметок по дате
    filtered_notes = []
    for note in notes:
        note_date = datetime.datetime.strptime(note['timestamp'], '%d-%m-%Y %H:%M:%S')
        if note_date.date() == date:
            filtered_notes.append(note)
    print_notes(filtered_notes)


def delete_note(notes, id, file_name): # Функция для удаления заметки
    for index, note in enumerate(notes):
        if note['id'] == id:
            del notes[index]
    save_notes_json(notes, file_name)


def main():  # Функция главного меню

    file_name = "notes.json"
    notes = read_notes_file(file_name)

    while True:
        print('Выберите действие:')
        print('1. Вывести все заметки')
        print('2. Вывести заметки за определенную дату')
        print('3. Вывести конкретную заметку')
        print('4. Добавить новую заметку')
        print('5. Редактировать заметку')
        print('6. Удалить заметку')
        print('7. Выход')

        choice = input('Ваш выбор: ')

        if choice == '1':
            print_notes(notes)

        elif choice == '2':
            date_str = input('Введите дату в формате ДД-ММ-ГГГГ: ')
            date = datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
            filter_by_date(notes, date)
            
        elif choice == '4':
            notes = add_note(notes)
            save_notes_json(notes, file_name)
            print('Заметка успешно добавлена')

        elif choice == '6':
            id = int(input('Введите ID заметки для удаления: '))
            notes = delete_note(notes, id)
            print(f'Заметка №{id} удалена')

        elif choice == '7':
            break

        else:
            print('Неверный выбор пункта меню')


if __name__ == '__main__':
    main()