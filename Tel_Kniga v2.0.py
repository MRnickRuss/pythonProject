d = dict()
def menu():
    choice = int(input("Введите 1 для добавления или изменения телефонного контакта\n"
                           "        2 для удаления телефонного контакта\n"
                           "        3 для вывода телефонной книги\n"
                           "        4 для выхода из программы\n"))
def add_number():
    print('Введите номер')
    number = input()
    new_number = number.lstrip('')
    if (len(new_number) > 12) or (len(new_number) < 10):
        print("Введен некорректный номер")
    if (number.startswith("9") is True) and (len(number) == 10):
        new_number = new_number.replace("9", "+79", 1)
    if number.startswith("7") is True:
        new_number = new_number.replace("7", "+7")
    if number.startswith("8") is True:
        new_number = new_number.replace("8", "+7")


def add_name():
    name = input("Введите имя: ")
    if  name.isupper():
        name.lower()
    d[name.title()] = new_number
    print(d)


def dictionary():
    number = add_number()
    name = add_name()


def delete():
    name = input("Выберите имя, которое хотите удалить: ")
    del d[name]
    print(d)

while True:
    choice = menu()
    if choice == 1:
        dictionary()
    elif choice == 2:
        delete()
    elif choice == 3:


        break