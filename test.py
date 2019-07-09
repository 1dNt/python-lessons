import sys
import os

args = sys.argv

def menu():
    result = input('Введите данные для генератора папок в формате:\n'
          '1. Список названий папок через запятую или \n'
          '2. "шаблон", кол-во (Будут созданы N папок с именем "шаблон_{1-N}")\n')
    return map(lambda x: int(x) if (x.isdigit()) else x, result.replace(' ','').split(','))

def make_dir(*f_args, **kwargs):
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
            dir_name += [f'{key}_{i}' for i in range(1, kwargs.get(key)+1)]
        make_dir(*dir_name)
    else:
        for id in f_args:
            dir_path = os.path.join(os.getcwd(), str(id))
            try:
                #os.mkdir(dir_path)
                print(id)
            except FileExistsError:
                print(f'Директория *\\{id} уже существует')

d = 'k','cnt=5'
print(d)
print(*d)
make_dir(*d)