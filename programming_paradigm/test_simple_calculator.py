# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely perform division with error handling.

    Args:
        numerator: The numerator, expected to be numeric or convertible to float.
        denominator: The denominator, expected to be numeric or convertible to float.

    Returns:
        str: The result of the division or an error message.
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            return "Error: Cannot divide by zero."

        result = numerator / denominator
        return f"The result of the division is {result:.2f}"

    except ValueError:
        return "Error: Please enter numeric values only."
