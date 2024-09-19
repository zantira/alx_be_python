
num1 = int(input("Enter first number: "))    

num2 = int(input("Enter second number: "))

select_operator = input("Choose the operation (+,-,*,/): ")

match select_operator:
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
    

