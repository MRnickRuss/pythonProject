print('Введите имя файла:')
a = []
try:
    file_name = input()
    f = open(file_name)
    count = int(f.readline())
    for i in range(count):
        b = f.readline().rstrip('\n')
        a.append(int(b))
    f.close()
    print(a)
except FileNotFoundError:
    print("Невозможно найти файл")
except EOFError:
    print('Неверное количество строк')
except IOError:
    print('Невозможно прочитать файл')
except TypeError:
    print('Невозможно преобразовать строку в число')
except:
    print('Неизвестная ошибка')
