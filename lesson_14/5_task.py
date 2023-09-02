# ------------------------------------------- 5 -----------------------------
"""
📌 На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину,
   а также вычисляющую периметр, площадь и позволяющий складывать и вычитать
   прямоугольники беря за основу периметр.
📌 Напишите 3-7 тестов unittest для данного класса.
"""

class Rectangle:

    def __init__(self, width, height=None):
        self._width = width
        if height is None:
            self._height = width
        else:
            self._height = height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError(f'Ширина должна быть положительной, а не  {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError(f'Высота должна быть положительной, а не  {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.r1 = Rectangle(1, 1)
        self.r2 = Rectangle(10, 20)
        self.r3 = Rectangle(20, 10)
        self.r4 = Rectangle(3, 5)

    def test_create(self):
        self.assertEqual(Rectangle(1, 1), self.r1)

    def test_perimetr(self):
        self.assertEqual(self.r2.perimeter(), 60)

    def test_area(self):
        self.assertEqual(self.r3.area(), 200)

    def test_perimetr_equal(self):
        self.assertEqual(self.r2.perimeter(), self.r3.perimeter())

    def test_area_no_equal(self):
        self.assertNotEqual(self.r3.area(), self.r4.area())

    def test_sum(self):
        self.assertEqual(self.r2 + self.r3, Rectangle(30, 30))

    def test_sub(self):
        self.assertEqual(self.r4 - self.r3, Rectangle(17, 5))


if __name__ == '__main__':
    unittest.main(verbosity=2)
