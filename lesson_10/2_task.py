# ------------------------------------------- 2 -----------------------------
"""
Создайте класс прямоугольник.
📌 Класс должен принимать длину и ширину при создании
экземпляра.
📌 У класса должно быть два метода, возвращающие периметр
и площадь.
📌 Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


spam = Rectangle(5, 2)
eggs = Rectangle(7)

print(f'{spam.area() =}')
print(f'{spam.perimeter()= }')
print(f'{eggs.area()= }')
print(f'{eggs.perimeter()= }')
