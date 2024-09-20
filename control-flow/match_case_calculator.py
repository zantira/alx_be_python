#program that uses Match Case statements for handling multiple operations in a simple calculator program.

num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

operator = input("Choose the operation (+,-,*,/): ")

match operator:
    case "+":
        print("The Results is", num1 + num2)
    case "-":
        print("The Results is", num1 - num2)
    case "*":
        print("The Results is", num1 * num2)
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("The Results is", num1 / num2)
    case "":
        print("invalid operator")