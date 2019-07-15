from math import sqrt


def len_lines(a, b):
    """
    Функция вычисления длины отрезка по координатам
    :param a: tuple(a, b)
    :param b: tuple(a, b)
    :return: float
    """
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
