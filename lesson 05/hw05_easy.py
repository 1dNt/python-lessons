# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def get_dir_name():
    """
    Выделяет список имен папок из введенных данных
    :return: list
    """
    temp = input('Введите названия папок, через пробел:\n')
    return temp.split(' ')

def make_dir(*f_args):
    """
    Функция создания каталогов в текущей директории
    Создает N каталогов, явно перечисленных на входе f_args
    :param f_args: *list
    :return: None
    """
    if f_args:
        idx = str()
        for id in f_args:
            dir_path = os.path.join(os.getcwd(), str(id))
            try:
                if id:
                    os.mkdir(dir_path)
                    idx += f'{id} '
            except FileExistsError:
                print(f'Директория *\\{id} уже существует')
        if idx:
            print(f'\nКаталоги созданы: {idx}')
    else:
        make_dir(*get_dir_name())

def del_dir(*f_args):
    """
    Функция удаления каталогов в текущей директории
    Удаляет N каталогов, явно перечисленных на входе f_args
    :param f_args: *list
    :return: None
    """
    if f_args:
        idx = str()
        for id in f_args:
            dir_path = os.path.join(os.getcwd(), str(id))
            try:
                if id:
                    os.rmdir(dir_path)
                    idx += f'{id} '
            except FileNotFoundError:
                print(f'Директория *\\{id} не найдена')
        if idx:
            print(f'\nКаталоги удалены: {idx}')
    else:
        del_dir(*get_dir_name())

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def view_dir(*args):
    """
    Функция просмотра содержимого директории
    :param args: Any (не используется, заглушка)
    :return: None
    """
    print('Содержимое директории:')
    for id in os.listdir():
        print(id)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

