import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3, 3), 8)
        self.assertEqual(self.calc.add(-1, 1, 0), 0)
        self.assertEqual(self.calc.add(-1, -1, -2), -4)


    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7, 2), 42)
        self.assertEqual(self.calc.multiply(-1, 1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1, -1), -1)


if __name__ == '__main__':
    unittest.main()
