import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area_zero(self):
        # Тест 1: проверяем, что площадь квадрата определяется верно при стороне 0
        self.assertEqual(area(0),0)

    def test_area_int(self):
        # Тест 2: Проверяем, что площадь квадрата определяется верно при целочисленом значение переменной
        self.assertEqual(area(4),16)

    def test_area_float(self):
        # Тест 3: Проверяем, что площадь квадрата определяется верно при вещественном значение переменной
        self.assertEqual(area(1.5),2.25)

    def test_perimeter_zero(self):
        # Тест 4: Проверяем, что периметр квадрата определяется верно при стороне 0
        self.assertEqual(perimeter(0),0)

    def test_perimeter_int(self):
        # Тест 5: Проверяем, что периметр квадрата определяется верно при целочисленом значение переменной
        self.assertEqual(perimeter(10),4*10)

    def test_perimeter_float(self):
        # Тест 6: Проверяем, что периметр квадрата определяется верно при вещественном значение переменной
        self.assertEqual(perimeter(2.5),4*2.5)



