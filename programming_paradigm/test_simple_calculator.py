# script to define and run unit tests for each method in the SimpleCalculator class

import unittest
from simple_calculator import SimpleCalculator

class Runtest(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()
        self.a = 4
        self.b = 2

    def test_addition(self):
        result = self.calc.add(self.a, self.b)
        self.assertEqual(self.calc.add(self))

    def test_add_negative(self):
        result = self.calc.add(-self.a, self.b)
        self.assertEqual(result, -2)

    def test_add_negative_negative(self):
        result = self.calc.add(-self.a, -self.b)
        self.assertEqual(result, -6)

    #unittest for subract() function
    
    def test_subtraction(self):
        result = self.calc.subtract(self.a , self.b)
        self.assertEqual(self.calc.subtract(self))

    def test_subtract(self):
        result = self.calc.subtract(-self.a, self.b)
        self.assertEqual(self.calc.subtract(self))

    def test_subtract_negative_negative(self):
        result = self.calc.subtract(-self.a, -self.b)
        self.assertEqual(result, -2)


    #unittest for multiply() function

    def test_multiply_positive(self):
        result = self.calc.multiply(self.a , self.b)
        self.assertEqual(result, 8)
    
    def test_multiply_negative(self):
        result = self.calc.multiply(-self.a, self.b)
        self.assertEqual(result, -8)


    #unittest for the divide() function

    def test_divide_positive(self):
        result = self.calc.divide(self.a, self.b)
        self.assertEqual(result, 2)

    def test_divide_negative(self):
        result  = self.calc.divide(-self.a, self.b)
        self.assertEqual(result, -2)

    def test_divide_zero_division(self): 
        result = self.calc.divide(self.a, self.b)
        if self.b == 0:
            self.assertEqual(result, "Cannot divide by zero")


if __name__ == "__main__":
    unittest.main()

    

