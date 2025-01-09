def perform_operation(num1: float, num2: float, operation: str):
    match operation:
        case 'add':
            result = num1 + num2
        case 'subtract':
            result = num1 - num2
        case 'multiply':
            result = num1 * num2
        case 'divide':
            if num1 == 0:
                return "Zero is not divisible."
        case _:
            return "Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."
    
    return result
