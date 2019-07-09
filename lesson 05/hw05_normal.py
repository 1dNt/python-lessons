# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os
import sys
import hw05_easy as hw5

args = sys.argv

def menu(*f_args):
    """
    Меню ключе в консоли.
    :param f_args: заглушка
    :return: None
    """
    print("""__________________________________________
Доступные ключи:
h: Справка.
cd *<имя директории>: Перейти в папку в текущей директории.
up: Вернуться на папку назад.
dir: Просмотреть содержимое текущей папки.
del *<перечень директорий>: Удалить папку.
make *<перечень директорий>: Создать папку.
Q: Выход.

* - не обязательный параметр
__________________________________________""")

def get_key(arg):
    """
    Выделяет ключ из списка введенных данных
    :param arg: list
    :return: list
    """
    try:
        return arg[0]
    except IndexError:
        return None

def get_dir_name1(arg):
    """
    Выделяет список имен папок из введенных данных
    :param arg: list
    :return: list
    """
    try:
        return arg[1:]
    except IndexError:
        return None

def change_dir(*f_args):
    """
    Функция изменения директории, с запросом имени подпапки
    :param f_args: имя вложенного каталога list
    :return: None
    """
    if f_args:
        try:
            os.chdir(os.path.join(os.getcwd(), str(f_args[0])))
            print(f'Успешно: {os.getcwd()}')
        except FileNotFoundError:
            print(f'Директория *\\{f_args[0]} не найдена')
    else:
        change_dir(input('Введите название папки:\n'))

def return_dir():
    """
    Функция возврата на папку вверх по каталогу
    :return: None
    """
    os.chdir(os.path.dirname(os.getcwd()))
    print(f'Успешно: {os.getcwd()}')


print(sys.argv)

try:
    key = sys.argv[1]
except IndexError:
    key = None
try:
    dir_name = sys.argv[2:]
except IndexError:
    dir_name = None

do = {
    'h': menu,
    'cd': change_dir,
    'up': return_dir,
    'dir': hw5.view_dir,
    'del': hw5.del_dir,
    'make': hw5.make_dir
}

while True:
    if key == 'Q':
        break
    elif do.get(key):
        do[key](*dir_name)
        key = dir_name = None
    else:
        ans = input('\nУкажите ключ. (h - для получения справки)\n')
        key = get_key(ans.split(' '))
        dir_name = get_dir_name1(ans.split(' '))