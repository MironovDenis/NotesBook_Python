def main():

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

        if choice == '7':
            break

        else:
            print('Неверный выбор пункта меню')
    
if __name__ == '__main__':
    main()


'''        elif choice == '2':

        elif choice == '3':

        elif choice == '4':

        elif choice == '5':

        elif choice == '6': 

        elif choice == '7':'''