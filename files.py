def main():
    file_name = "text_file.txt"

    while True:
        print("\nВыберите действие:")
        print("1. Записать текст в файл")
        print("2. Прочитать текст из файла")
        print("3. Очистить содержимое файла")
        print("4. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == '1':
            text = input("Введите текст для записи в файл: ")
            with open(file_name, 'a') as file:
                file.write(text + '\n')
            print("Текст успешно записан в файл.")

        elif choice == '2':
            try:
                with open(file_name, 'r') as file:
                    contents = file.read()
                    print("Содержимое файла:\n", contents)
            except FileNotFoundError:
                print("Файл не найден.")

        elif choice == '3':
            with open(file_name, 'w') as file:
                file.write('')
            print("Содержимое файла очищено.")

        elif choice == '4':
            print("Вы вышли из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()