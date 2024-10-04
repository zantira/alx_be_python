#division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.

def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Please enter numeric values only")