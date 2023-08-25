# ------------------------------------------- 5 -----------------------------
"""
📌 Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.
"""


class Rectangle:
    __slots__ = ('_width', '_height')

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative.")
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)


rectangle = Rectangle(4, 5)
print("Width:", rectangle.width)
print("Height:", rectangle.height)
print("Area:", rectangle.area)
print("Perimeter:", rectangle.perimeter)

rectangle.width = 6
rectangle.height = 8
print("Updated Width:", rectangle.width)
print("Updated Height:", rectangle.height)
print("Updated Area:", rectangle.area)
print("Updated Perimeter:", rectangle.perimeter)

try:
    rectangle.width = -2
except ValueError as e:
    print("Error:", e)

try:
    rectangle.height = -3
except ValueError as e:
    print("Error:", e)
