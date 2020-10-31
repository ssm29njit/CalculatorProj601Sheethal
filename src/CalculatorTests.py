import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 9)

    def test_add_method_calculator(self):
        test_data = CsvReader('UnitTestAddition.csv').data
        pprint(test_data)

        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    # def test_subtract_method_calculator(self):
    #     self.assertEqual(self.calculator.subtract(2, 2), 0)
    #     self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        test_data = CsvReader('UnitTestMultiplication.csv').data
        pprint(test_data)

        self.assertEqual(self.calculator.multiply(2,3), 6)
        self.assertEqual(self.calculator.result, 6)


    '''def test_divide_method_calculator(self):
        test_data = CsvReader('UnitTestDivision.csv').data
        pprint(test_data)
        self.assertEqual(self.calculator.divide(15,3), 5)
        self.assertEqual(self.calculator.result, 5)
    '''

    def test_square_method_calculator(self):
        test_data = CsvReader('UnitTestSquare.csv').data
        pprint(test_data)
        self.assertEqual(self.calculator.square(3), 9)
        self.assertEqual(self.calculator.result, 9)


if __name__ == '__main__':
    unittest.main()