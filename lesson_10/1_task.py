# ------------------------------------------- 1 -----------------------------
"""
Создайте класс окружность.
📌 Класс должен принимать радиус окружности при создании
экземпляра.
📌 У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""

from math import pi
from random import randint


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius * self.radius


n = Circle(7)
print(n.perimeter())
print(n.area())
