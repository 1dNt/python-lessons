#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.


Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random


class Ticket:

    def __init__(self, name):
        self.__ticket = self.__get_ticket
        self.name = name

    @property
    def __get_ticket(self):
        """
        Генерируем карточку 9х5 с 5 рандомными числами от 1 до 90 в линии
        (в пустые ячейки записыватся None)
        :return: list
        """
        card = []  # Карточка
        nums = sorted(random.sample(range(1, 91), 15))  # Выборка чисел для карточки
        patt = [1, 1, 1, 1, 1, 0, 0, 0, 0]  # Шаблон одной линии в карте, 1 - ячейка с числом, 0 - пустая ячейка
        for i in range(3):
            random.shuffle(patt)  # Перемешиваем шаблон заполнения ячеек
            tmp = sorted([nums.pop(nums.index(random.choice(nums))) for _ in range(5)])  # Сортируем содержимое линии
            for id in patt:  # Заполняем линию согласно обновленному шаблону
                if id:
                    card.append(tmp.pop(0))
                else:
                    card.append('')
            card.append('\n')  # Перевод строки в конце каждой линии для корректной печати на экране
        card.pop()  # Удаление последнего перевода строки
        return card

    def check_number(self, num: int):
        """
        Проверяем наличие выпавшего числа в билете
        :param num: int
        :return: bool
        """
        try:
            self.__ticket[self.__ticket.index(num)] = '-'
            return True
        except ValueError:
            return False

    def check_number_cheat(self, num: int):  # Метод нужен для отладки
        return num in self.__ticket

    @property
    def check_wins(self):
        """
        Проверяем закрылись ли все ячейки в билете
        :return: bool
        """
        return self.__ticket.count('-') == 15

    @property
    def _get_card(self):
        """
        Печатаем карточку в консоль cо всеми выравниваниями
        :return: None
        """
        tmp = [str(itm).rjust(2) for itm in self.__ticket]
        print(f'{self.name.center(28, "-")}')
        print('', *tmp)
        print(f'{"-" * 28}')


class Game:

    def __init__(self, number: int):
        self.number = number
        self.user = Ticket('Ваша карточка')  # Формируем карту игрока
        self.comp = Ticket('Карточка компьютера')  # Формируем карту компьютера
        self.nums = random.sample(range(1, 91), 90)  # Формируем "мешок" с рандомными бочонками от 1 до 90
        self.winner = None
        self.turn = 0

    @property
    def start(self):
        """
        Метод запускающий игру
        Циклически перебирает внутренние методы, пока не объявится проигравший
        :return: bool
        """
        print('Игра началась!\n')
        print('Игоровые карточки:\n')
        self.user._get_card
        self.comp._get_card
        input('Нажмите Enter, чтобы начать.')
        while not self.winner:
            game = self.__run_level
        print(self.winner)
        return game

    @property
    def __get_number(self):
        """
        Извлекает рандомное число от 1 до 90 из списка nums экземпляра Game
        :return: int
        """
        random.shuffle(self.nums)
        return self.nums.pop()

    @property
    def __run_level(self):
        """
        Метод прохода очередного тура
        Определяет победителя
        :return: bool
        """
        self.turn += 1
        num = self.__get_number
        print(f'\nTurn {self.turn}:\nНовый бочонок: {num} (осталось {len(self.nums)})')
        print(self.user.check_number_cheat(num))  # Используется для отладки
        self.user._get_card
        self.comp._get_card
        ans = input('Зачеркнуть цифру? (y/n)\n')
        res = self.__logic(ans, num)  # Выносим логику проверки числа в отдельный метод
        if res:
            if self.user.check_wins:  # Проверяем выиграл ли игрок
                self.winner = 'Вы выиграли'
                return True
            elif self.comp.check_wins:  # Проверяем выиграл ли компьютер
                self.winner = 'Вы проиграли'
                return False
        else:
            self.winner = 'Вы проиграли'
            return False

    def __logic(self, ans, num):
        """
        Метод проверки уловий и рез-та очередного хода
        :param ans: str
        :param num: int
        :return: bool
        """
        while True:
            if ans == 'y':
                res = self.user.check_number(num)
                self.comp.check_number(num)
                break
            elif ans == 'n':
                res = not self.user.check_number(num)
                self.comp.check_number(num)
                break
            else:
                ans = input('Введите y или n:\n')
        return res

    @property
    def get_winner(self):
        """
        Метод вывода победителя игры
        :return: str
        """
        if self.winner == 'Вы выиграли':
            return 'Игрок'
        return 'Компьютер'

    def __str__(self):
        """
        Вывод результата игры
        :return: str
        """
        return f'В игре {self.number} выиграл {self.get_winner.lower()} за {self.turn} ходов'


if __name__ == '__main__':

    game_1 = Game(1)
    game_1.start
    print(game_1.get_winner)
    print(game_1)
