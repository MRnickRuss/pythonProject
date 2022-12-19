import os
from pdf2docx import parse
from docx2pdf import convert
from PIL import Image


def correctnumber(min, max):
    n = int(input('\nВведите число: '))
    if int(n) <= max and int(n) >= min:
        return int(n)
    print(f'\nВведите число от {min} до {max}')
    return correctnumber(min, max)


def menu():
    print('\nВыберите действие:\n'
          '0 - Сменить рабочий каталог\n'
          '1 - Преобразовать PDF в Docx\n'
          '2 - Преобразовать Docx в PDF\n'
          '3 - Произвести сжатие изображения\n'
          '4 - Удалить группу файлов\n'
          '5 - Выход')
    return correctnumber(0, 5)


def changedir():
    path = input('\nУкажите путь к каталогу: ')
    try:
        os.chdir(path)
    except:
        print('\nНеверный путь')
        changedir()
    return os.getcwd()


def find(dir, size):
    files = []
    for file in os.listdir(dir):
        if os.path.isfile(file):
            if size.__contains__(file.split('.')[-1]):
                files.append(file)
    for i in range(len(files)):
        print(f'{i + 1} - {files[i]}')
    return files


def choose(files):
    print('\nВыберите файл для конвертации или нажмите 0 - для конвертации всех файлов):')
    file_num = correctnumber(0, len(files))
    if file_num == 0:
        for file in files:
            convert(file)
    else:
        convert(files[file_num - 1])


def convert(file):
    format_file = file.split('.')[-1]
    if format_file == 'pdf':
        new_file = file.replace(format_file, 'docx')
        try:
            parse(file, new_file)
        except:
            print(f'Невозможно преобразовать файл {file} в формат docx')
    elif format_file == 'doc' or format_file == 'docx':
        new_file = file.replace(format_file, 'pdf')
        try:
            convert(file, new_file)
        except:
            print(f'Невозможно преобразовать файл {file} в формат pdf')
    else:
        print('\nУкажите параметры сжатия в %:')
        quality = correctnumber(1, 100)
        try:
            image_path = file
            image_file = Image.open(image_path)
            image_file.save(file, quality=quality)
        except:
            print(f'Невозможно сжать изображение')


def change(dir, format):
    files = find(dir, format)
    if len(files) == 0:
        print(f'\nВ папке нет файлов формата {", ".join(format)}')
        return
    choose(files)


def deleteall():
    print('\nВыберите действие:\n'
          '1 - Удалить все файлы начинающиеся с подстроки\n'
          '2 - Удалить все файлы заканчивающиеся на подстроку\n'
          '3 - Удалить все файлы содержащие подстроку\n'
          '4 - Удалить все файлы по расширению')
    return correctnumber(1, 4)


catalog = os.getcwd()
print(f'Текущий каталог: {catalog}')
while True:
    option = menu()
    if option == 0:
        catalog = changedir()
        print(f'Текущий каталог: {catalog}')
    if option == 1:
        change(catalog, ['pdf'])
    if option == 2:
        change(catalog, ['doc', 'docx'])
    if option == 3:
        change(catalog, ['img', 'png', 'jpg', 'jpeg', 'bmp'])
    if option == 4:
        delete_option = deleteall()
        sub_string = input('Введите подстроку: ')
        files = []
        for file in os.listdir(catalog):
            if os.path.isfile(file):
                files.append(file)
        delete_files = []
        if delete_option == 1:
            for file in files:
                if file[0:len(sub_string)] == sub_string:
                    delete_files.append(file)
        if delete_option == 2:
            for file in files:
                filename = file.split('.')[0]
                if filename[-len(sub_string):] == sub_string:
                    delete_files.append(file)
        if delete_option == 3:
            for file in files:
                filename = file.split('.')[0]
                if filename.__contains__(sub_string):
                    delete_files.append(file)
        if delete_option == 4:
            for file in files:
                format = file.split('.')[1]
                if format == sub_string:
                    delete_files.append(file)
        print(f'Вы действительно хотите удалить файлы(да/нет)?')
        print("\n".join(delete_files))
        while True:
            answer = input()
            if answer == 'да':
                for file in delete_files:
                    os.remove(file)
                print(f'Файлы успешно удалены')
                break
            elif answer == 'нет':
                break
    if option == 5:
        break
