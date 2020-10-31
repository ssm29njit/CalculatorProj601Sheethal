import unittest
from Calculator import Calculator, addition

class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEquals(calculator.result,4)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEquals(calculator.add(2,2), 4)

if __name__ == '__main__':
    unittest.main()
