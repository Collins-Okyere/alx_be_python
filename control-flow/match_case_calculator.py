num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = input("Choose the operation (+, -, *, /): ")
match result:
    case "+":
        print(f"The result is {num1 + num2}.")
    case "-":
        print(f"The result is {num1 - num2}.")
    case "*":
        print(f"The result is {num1 * num2}.")
    case "/":
        if num2 != 0:
            print(f"The result is {num1 / num2}.")
        else:
            print(f"Cannot divide by zero.")

