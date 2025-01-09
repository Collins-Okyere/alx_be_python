def perform_operation(num1: float, num2: float, operation: str):
    # Check the operation and perform the corresponding arithmetic operation
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num1 == 0:
            return "Zero is not divisible."
    else:
        return "Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."
    
    return result
