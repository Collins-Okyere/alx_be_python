# def perform_operation(num1, num2, operation):
#     match operation:
#         case 'add':
#             result = num1 + num2
#         case 'subtract':
#             result = num1 - num2
#         case 'multiply':
#             result = num1 * num2
#         case 'divide':
#             if num1 == 0:
#                 return "Zero is not divisible."
#         case _:
#             return "Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."
    
#     return result


# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    # Perform arithmetic operations based on the operation parameter
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Invalid operation"
