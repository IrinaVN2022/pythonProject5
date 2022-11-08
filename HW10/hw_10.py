# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від
# "Транспортний засіб".
# Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".


class Vehicle:

    def __init__(self, name, color, price):
        """ initialized the value of attributes"""
        self.name = name
        self.color = color
        self.price = price

    def info(self):
        """provides information about the object by attributes"""
        print(self.name, self.color, self.price)


class Car(Vehicle):

    def change_gear(self, no):
        """shifts gear"""
        print(self.name, 'change_gear', no)


car = Car('BMW X6', 'Black', 95000)

car.info()
car.change_gear(5)


class Plane(Vehicle):
    def gain_height(self, hg):
        """altitude gain function"""
        print(self.name, 'gain_height, m', hg)


plane = Plane('F35 Lightning', 'Grey', 55100000)

plane.info()
plane.gain_height(3000)


class Ship(Vehicle):
    def gain_speed(self, speed):
        """speed dial function"""
        print(self.name, 'gain_speed, km/h', speed)


ship = Ship('Nimitz', 'White', 2300000)

ship.info()
ship.gain_speed(56)
