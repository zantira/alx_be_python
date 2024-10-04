#division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.
import sys
def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        sys.exit(1)

    except ValueError:
        print("Error: Please enter numeric values only.")
        sys.exit(1)
    