# script to define and run unit tests for each method in the SimpleCalculator class

import unittest
from simple_calculator import SimpleCalculator

class Runtest(unittest.TestCase):

    def setUp(self):
        self.calculator = SimpleCalculator()
        self.a = 4
        self.b = 2

    def test_add_postive(self):
        result = self.calculator.add(self.a, self.b)
        self.assertEqual(result, 6)

    def test_add_negative(self):
        result = self.calculator.add(-self.a, self.b)
        self.assertEqual(result, -2)

    def test_add_negative_negative(self):
        result = self.calculator.add(-self.a, -self.b)
        self.assertEqual(result, -6)

    #unittest for subract() function
    
    def test_subtract_positive(self):
        result = self.calculator.subtract(self.a , self.b)
        self.assertEqual(result, 2)

    def test_subtract_negative(self):
        result = self.calculator.subtract(-self.a, self.b)
        self.assertEqual(result, -6)

    def test_subtract_negative_negative(self):
        result = self.calculator.subtract(-self.a, -self.b)
        self.assertEqual(result, -2)


    #unittest for multiply() function

    def test_multiply_positive(self):
        result = self.calculator.multiply(self.a , self.b)
        self.assertEqual(result, 8)
    
    def test_multiply_negative(self):
        result = self.calculator.multiply(-self.a, self.b)
        self.assertEqual(result, -8)


    #unittest for the divide() function

    def test_divide_positive(self):
        result = self.calculator.divide(self.a, self.b)
        self.assertEqual(result, 2)

    def test_divide_negative(self):
        result  = self.calculator.divide(-self.a, self.b)
        self.assertEqual(result, -2)

    def test_divide_zero_division(self): 
        result = self.calculator.divide(self.a, self.b)
        if self.b == 0:
            self.assertEqual(result, "Cannot divide by zero")


if __name__ == "__main__":
    unittest.main()

    

