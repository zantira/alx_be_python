#class_static_methods_demo.py. In this script, define a class Calculator that includes both a class method and a static method to perform calculations. This task aims to illustrate when and how to use @classmethod and @staticmethod decorators, highlighting their differences and practical applications.


class Calculator:
    calculation_type = "Arithmetic Operations"
    def __init__(self):
        pass

    @classmethod
    def multiply(cls, a, b):
        
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
    @staticmethod
    def add(a, b):
        return a + b
    


from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()



