from CsvReader import CsvReader
import math

def addition(a, b):
    return float(a) + float(b)

def subtraction(a, b):
    return float(a) - float(b)

def multiplication(a, b):
    return float(a) * float(b)

def division(a, b):
    return float(a) / float(b)

def squaring(a):
    return float(a) * float(a)

def rooting(a):
    return math.sqrt(a)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    # def subtract(self, a, b):
    #     self.result = subtraction(a, b)
    #     return self.result

    def multiply(self, a, b):
        self.result=multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result=division(a, b)
        return self.result

    def square(self, a):
        self.result = squaring(a)
        return self.result

    def root(self, a):
        self.result = rooting(a)
        return self.result