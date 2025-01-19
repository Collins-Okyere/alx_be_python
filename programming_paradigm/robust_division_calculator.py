def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero and non-numeric inputs.

    :param numerator: The numerator for division.
    :param denominator: The denominator for division.
    :return: A string with the result or an appropriate error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divise by zero."
    return f"The result of the division is {result}"

def main():
    if len(syn.argv) !=3:
        print("Usag: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)
if __name__ == "__main__":
    main()
