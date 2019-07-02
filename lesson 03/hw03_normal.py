# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print('------------\nЗадача-1:\n')

def fibonacci(n=1, m=2):
    """
    Функция вычисления ряда фибоначи от n до m
    :param n: int
    :param m: int
    :return: list
    """
    a = 0
    b = c = 1
    f = []
    for i in range(0, m):
        if i < n-1:
            c = a + b
            a, b = b, c
        else:
            f.append(c)
            c = a + b
            a, b = b, c
    return f

print(fibonacci(5, 15))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print('------------\nЗадача-2:\n')

def sort_to_max(origin_list):
    """
    Функция сортировки списков
    :param origin_list: lst
    :return: lst
    """
    id = 1
    dig_list = [itm for itm in origin_list if type(itm) == int or type(itm) == float]
    str_list = [itm for itm in origin_list if type(itm) == str]
    while id < len(dig_list):
        if dig_list[id-1] > dig_list[id]:
            dig_list[id-1], dig_list[id] = dig_list[id], dig_list[id-1]
            id = 1
        else:
            id += 1
    id = 1
    while id < len(str_list):
        if str_list[id-1] > str_list[id]:
            str_list[id-1], str_list[id] = str_list[id], str_list[id-1]
            id = 1
        else:
            id += 1
    return dig_list + str_list

lst = [2, 'ac', 10, 'лошадь', -12, 'a', 2.5, '-+=', 20, -11, 4, 'ab', 4, 0]
print(lst)
print(sort_to_max(lst))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print('------------\nЗадача-3:\n')

def filt(func, iter):
    """
    Кастомная версия функии filter
    :param func: функция возвращающая True or False
    :param iter: последовательность(list/tuple etc)
    :return: list
    """
    return [id for id in iter if func(id)]

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a)
print(filt((lambda x: x if (x%2 == 0) else 0), a))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print('------------\nЗадача-4:\n')

import math

def paral(a,b,c,d):
    """
    Проверка точек параллелограмма
    :param a: tuple(a, b)
    :param b: tuple(a, b)
    :param c: tuple(a, b)
    :param d: tuple(a, b)
    :return: bool
    """
    ch = (math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) == math.sqrt((c[0] - d[0]) ** 2 + (c[1] - d[1]) ** 2) and \
          math.sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2) == math.sqrt((b[0] - d[0]) ** 2 + (b[1] - d[1]) ** 2))

    ch2 = (math.sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2) == math.sqrt((b[0] - d[0]) ** 2 + (b[1] - d[1]) ** 2) and \
           math.sqrt((a[0] - d[0]) ** 2 + (a[1] - d[1]) ** 2) == math.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2))

    ch3 = (math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) == math.sqrt((c[0] - d[0]) ** 2 + (c[1] - d[1]) ** 2) and \
           math.sqrt((a[0] - d[0]) ** 2 + (a[1] - d[1]) ** 2) == math.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2))
    return ch or ch2 or ch3

A1 = (4,4)
A2 = (9,4)
A3 = (2,1)
A4 = (7,1)
print(f'1й набор {A1, A2, A3, A4}: {paral(A1,A2,A3,A4)}')

A1 = (5,4)
A2 = (9,4)
A3 = (5,1)
A4 = (7,1)
print(f'2й набор {A1, A2, A3, A4}: {paral(A1,A2,A3,A4)}')