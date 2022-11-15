# Доопрацюйте класс Triangle з попередньої домашки наступним чином:
# обʼєкти классу Triangle можна порівнювати між собою (==, !=, >, >=, <, <=) за площею.
# Перетворення обʼєкту классу Triangle на стрінг показує координати його вершин у форматі x1, y1 -- x2, y2 -- x3, y3
from math import sqrt


class Point:

    def __init__(self, x=0, y=0):
        """ initialized the value of attributes,implements data validation """
        if (not isinstance(x, int) and not isinstance(x, float)) or (
                not isinstance(y, int) and not isinstance(y, float)):
            raise TypeError  # coordinate can't be string
        else:

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
        else:

            self._first = first_point
            self._second = second_point
            self._third = third_point

    def __eq__(self, other):
        return self.square == other.square

    def __lt__(self, other):
        return self.square < other.square

    def __str__(self):
        return f'Object of Triangle with coordinates: x1={self._first.x}, y1={self._first.y}, x2={self._second.x},' \
               f'y2={self._second.y}, x3={self._third.x}, y3={self._third.y}'

    @property
    def square(self):
        """calculates the area of a triangle"""

        a = sqrt((self._first.x - self._second.x) ** 2 + (self._first.y - self._second.y) ** 2)
        b = sqrt((self._second.x - self._third.x) ** 2 + (self._second.y - self._third.y) ** 2)
        c = sqrt((self._first.x - self._third.x) ** 2 + (self._first.y - self._third.y) ** 2)
        s = (a + b + c) / 2
        res = sqrt(s * (s - a) * (s - b) * (s - c))
        return round(res, 2)


Triangle2 = Triangle(p1, p2, p3)
print(Triangle2.square)
Triangle1 = Triangle(p4, p5, p6)
print(Triangle1.square)

if not Triangle1 < Triangle2:
    if Triangle1 == Triangle2:
        print('Squares are equal')
    else:
        print('Triangle1 > Triangle2')
else:
    print('Triangle1 < Triangle2')

print(Triangle1)