num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
ops = input("Choose the operation (+, -, *, /): ")
match ops:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
    print(f"The result is {result}.")
