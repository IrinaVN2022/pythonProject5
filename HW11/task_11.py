# 1. Доопрацюйте класс Point так, щоб в атрибутаx та y обʼєктів цього класу можна було записати тільки обʼєкти
# класу int або float
# 2. Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point).
# Реалізуйте перевірку даних, аналогічно до класу Line. Визначет атрибут, що містить площу трикутника
# (за допомогою property). Для обчислень можна використати формулу Герона
# (https://en.wikipedia.org/wiki/Heron%27s_formula)

from math import sqrt


class Point:

    def __init__(self, x=0, y=0):
        """ initialized the value of attributes,implements data validation """
        if (not isinstance(x, int) and not isinstance(x, float)) or (
                not isinstance(y, int) and not isinstance(y, float)):
            raise TypeError  # coordinate can't be string

        self.x = x
        self.y = y


p1 = Point(0, 0)
p2 = Point(4, 0)
p3 = Point(4, 6)
p4 = Point(2, 2)
p5 = Point(11, 4)
p6 = Point(7, 6)


class Triangle:
    _first = None
    _second = None
    _third = None

    def __init__(self, first_point, second_point, third_point):
        """ initialized the value of attributes,implements data validation """
        if not isinstance(first_point, Point) or not isinstance(second_point, Point) \
                or not isinstance(third_point, Point):
            raise TypeError  # argument must be Point
        self._first = first_point
        self._second = second_point
        self._third = third_point

    @property
    def square(self):
        """calculates the area of a triangle"""

        a = sqrt((self._first.x - self._second.x) ** 2 + (self._first.y - self._second.y) ** 2)
        b = sqrt((self._second.x - self._third.x) ** 2 + (self._second.y - self._third.y) ** 2)
        c = sqrt((self._first.x - self._third.x) ** 2 + (self._first.y - self._third.y) ** 2)
        s = (a + b + c) / 2
        res = sqrt(s * (s - a) * (s - b) * (s - c))
        return round(res, 2)


Triangle1 = Triangle(p1, p2, p3)
print(Triangle1.square)
Triangle2 = Triangle(p4, p5, p6)
print(Triangle2.square)
