# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import my_lib.geo as geo
from math import sqrt, acos, degrees


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        s = sqrt(self.perimeter() / 2 *
                 (self.perimeter() / 2 - geo.len_lines(self.a, self.b)) *
                 (self.perimeter() / 2 - geo.len_lines(self.b, self.c)) *
                 (self.perimeter() / 2 - geo.len_lines(self.c, self.a))
                 )
        return s

    def height(self, x, y):
        """
        Высчитывает высоту по основанию XY
        :param x: координаты точки X основания XY {tuple/list}
        :param y: координаты точки Y основания XY {tuple/list}
        :return: float
        """
        h = 2 * self.square() / geo.len_lines(x, y)
        return h

    def perimeter(self):
        p = geo.len_lines(self.a, self.b) + geo.len_lines(self.b, self.c) + geo.len_lines(self.c, self.a)
        return p

    def angle(self, x):
        """
        Высчитывает угол вершины X в радианах
        :param x: координаты вершины X {tuple/list}
        :return: float (radians)
        """
        temp = [self.a, self.b, self.c]
        try:
            temp.remove(x)
            ang = acos((geo.len_lines(x, temp[0]) ** 2 +
                        geo.len_lines(x, temp[1]) ** 2 -
                        geo.len_lines(temp[0], temp[1]) ** 2) /
                       (2 * geo.len_lines(x, temp[0]) * geo.len_lines(x, temp[1]))
                       )
            return ang
        except ValueError:
            print('Вершина не принадлежит фигуре')


a = (0, 0)
b = (4, 10)
c = (8, 10)
d = (12, 0)

figure1 = Triangle(a, b, c)
print(f'Периметр треугольника: {round(figure1.perimeter(), 2)}\n'
      f'Площадь треугольника: {round(figure1.square(), 2)}\n'
      f'Высота по основанию АВ: {round(figure1.height(a, b), 2)}\n'
      f'Высота по основанию ВС: {round(figure1.height(b, c), 2)}\n'
      f'Высота по основанию АС: {round(figure1.height(a, c), 2)}\n'
      f'Угол А равен: {round(degrees(figure1.angle(a)), 5)}\n')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapez(Triangle):
    def __init__(self, a, b, c, d):
        self.d = d
        Triangle.__init__(self, a, b, c)

    def isequi(self):
        t1 = geo.len_lines(self.a, self.c) == geo.len_lines(self.b, self.d)
        t2 = geo.len_lines(self.a, self.d) == geo.len_lines(self.b, self.c)
        t3 = geo.len_lines(self.a, self.b) == geo.len_lines(self.c, self.d)
        return t1 or t2 or t3

    def perimeter(self):
        return round(sum(self.len_side()), 3)

    def len_side(self, arg=None):
        tmp = (self.a, self.b, self.c, self.d)
        dict = {
            'a': 2,
            'b': 0,
            'c': 1,
            'd': 3,
        }
        lines = [round(geo.len_lines(tmp[idx - 1], itm), 3) for idx, itm in enumerate(tmp)]
        if dict.get(arg):
            return lines[dict.get(arg)]
        else:
            return lines

    @property
    def square(self):
        s = ((self.len_side()[2] + self.len_side()[0]) / 2) * \
            sqrt(self.len_side()[1] ** 2 - (
                    ((self.len_side()[0] - self.len_side()[2]) ** 2
                     + self.len_side()[1] ** 2
                     - self.len_side()[3] ** 2) /
                    (2 * (self.len_side()[0] - self.len_side()[2]))) ** 2
                 )
        return round(s, 2)


figure2 = Trapez(a, b, c, d)
print(f'Равнобедренная трапеция? - {figure2.isequi()}')
print(f'Длины сторон b/c/a/d: {figure2.len_side()}')
print(f'Периметр трапеции: {figure2.perimeter()}')
print(f'Площадь трапеции: {figure2.square}')
