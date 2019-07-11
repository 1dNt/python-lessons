# Функции для иморта в normal

import os


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
        make_dir(*input('Введите названия папок, через пробел:\n').split(' '))


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
        del_dir(*input('Введите названия папок, через пробел:\n').split(' '))


def view_dir(*args):
    """
    Функция просмотра содержимого директории
    :param args: Any (не используется, заглушка)
    :return: None
    """
    print('Содержимое директории:')
    for id in os.listdir():
        print(id)


if __name__ == "__main__":
    # Задача-1:
    # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
    # из которой запущен данный скрипт.
    # И второй скрипт, удаляющий эти папки.
    print('Задача-1')


    def mk_dir(*f_args, **kwargs):
        """
        Функция создания папок в текущей директории.
        Создает N кол-во папок (N задается после шаблона названия через знак =)
        :param f_args: Список названий папок (единичнычй экземпляр)
        :param kwargs: Словарь формата "шаблон_назв{str/int}=кол_экз{int}"
        :return: None
        """
        if kwargs:
            dir_name = list(f_args)
            for key in kwargs:
                dir_name += [f'{key}_{i}' for i in range(1, kwargs.get(key) + 1)]
            mk_dir(*dir_name)
        else:
            idx = str()
            for id in f_args:
                dir_path = os.path.join(os.getcwd(), str(id))
                try:
                    os.mkdir(dir_path)
                    idx += f'{id} '
                except FileExistsError:
                    print(f'Директория *\\{id} уже существует')
            if idx:
                print(f'\nКаталоги созданы: {idx}')


    def rm_dir(*f_args, **kwargs):
        """
        Функция создания папок в текущей директории.
        Создает N кол-во папок (N задается после шаблона названия через знак =)
        :param f_args: Список названий папок (единичнычй экземпляр)
        :param kwargs: Словарь формата "шаблон_назв{str/int}=кол_экз{int}"
        :return: None
        """
        if kwargs:
            dir_name = list(f_args)
            for key in kwargs:
                dir_name += [f'{key}_{i}' for i in range(1, kwargs.get(key) + 1)]
            rm_dir(*dir_name)
        else:
            idx = str()
            for id in f_args:
                dir_path = os.path.join(os.getcwd(), str(id))
                try:
                    os.rmdir(dir_path)
                    idx += f'{id} '
                except FileNotFoundError:
                    print(f'Директория *\\{id} не найдена')
            if idx:
                print(f'\nКаталоги удалены: {idx}')


    mk_dir(Dir=9)

    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.
    print('Задача-2')
    print('Текущие папки в директории:')
    for id in [itm for itm in os.listdir() if os.path.isdir(os.path.join(os.getcwd(), str(itm)))]:
        print(id)

    rm_dir(Dir=9)

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


