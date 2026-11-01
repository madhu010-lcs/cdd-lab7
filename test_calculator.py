import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.add(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(calculator.subtract(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(calculator.multiply(10, 5), 50)

    def test_division(self):
        self.assertEqual(calculator.divide(10, 5), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10, 0)


if __name__ == '__main__':
    unittest.main()