# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in a readable format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, number_of_days):
    """Calculate the future date by adding a given number of days to the current date."""
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    """Main function to demonstrate datetime functionalities."""
    # Part 1: Display the current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate a future date
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, number_of_days)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
