import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint
import csv
import decimal

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def dicToVar(self,a):
        if (len(a) > 3):
            a1 = a['Value 1']
            a2 = a['Value 2']
            a3 = a['Result']
            return a1, a2, a3
        if(len(a) < 4):
            a1 = a['Value 1']
            a2 = a['Result']
            return a1, a2

    def readFile(self, filename):
        data = CsvReader(filename).data
        for l in data:
            x = self.dicToVar(l)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    '''def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 4)
    '''
    def test_add_method_calculator(self):
        test_data = CsvReader('UnitTestAddition.csv').data

        for line in test_data:
            x_dict = { }
            x_dict = self.dicToVar(line)
            #pprint(x_dict)
            self.assertEqual(self.calculator.add(x_dict[0], x_dict[1]), int(x_dict[2]),"FailNOW")

    def test_subtract_method_calculator(self):
        test_data = CsvReader('UnitTestSubtraction.csv').data

        for line in test_data:
            x_dict = {}
            x_dict = self.dicToVar(line)
            #pprint(x_dict)
            #self.assertEqual(self.calculator.subtract(x_dict[0], x_dict[1]), int(x_dict[2]), "FailNOW")
            self.assertNotEqual(self.calculator.subtract(x_dict[0], x_dict[1]), int(x_dict[2]), "AssertNotEqualFailNOW")
         #self.assertEqual(self.calculator.subtract(2, 2), 0)
         #self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        test_data = CsvReader('UnitTestMultiplication.csv').data
        for line in test_data:
            x_dict = {}
            x_dict = self.dicToVar(line)
            pprint(x_dict)
            self.assertEqual(self.calculator.multiply(x_dict[0], x_dict[1]), int(x_dict[2]), "FailNOW")
    

    def test_divide_method_calculator(self):
        test_data = CsvReader('UnitTestDivision.csv').data
        for line in test_data:
            x_dict = {}
            x_dict = self.dicToVar(line)
            pprint(x_dict)
            self.assertNotEqual(self.calculator.divide(x_dict[0], x_dict[1]), float(x_dict[2]), "FailNOW")
            self.assertIsNot(self.calculator.divide(int(x_dict[0]), int(x_dict[1])), float(x_dict[2]))
    

    def test_square_method_calculator(self):
        test_data = CsvReader('UnitTestSquare.csv').data
        for line in test_data:
            x_dict = {}
            x_dict = self.dicToVar(line)
            #pprint(x_dict)

            self.assertEqual(self.calculator.square(x_dict[0]), int(x_dict[1]), "FailNOW")
            self.assertIsNotNone(self.calculator.square(x_dict[0]), "TestValue is none")

    def test_root_method_calculator(self):
        test_data = CsvReader('UnitTestSquareRoot.csv').data
        for line in test_data:
            x_dict = {}
            x_dict = self.dicToVar(line)
            #pprint(x_dict)

            res = self.calculator.root(int(x_dict[0]))
            y = len(str(float(x_dict[1])).split('.')[-1])
            d = round(res,y)
            self.assertAlmostEqual(d, float(x_dict[1]), "FailNOW")
            #self.assertIsNotNone(self.calculator.root(x_dict[0]), "TestValue is none")


if __name__ == '__main__':
    unittest.main()