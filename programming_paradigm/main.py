import sys

from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage python main.py <numerator> <denominator>")
        sys.exit(1)
    
        numerator = float(sys.argv[1])
        denominator = float(sys.argv[2])
    
        sys.exit(1)

    result = safe_divide(numerator, denominator)
    if result is not None:
        print(f"The result of the division is {result}")

if __name__ == "__main__":
    main()


